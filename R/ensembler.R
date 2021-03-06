#' Create ensemble of derivatives.
#' 
#' @param data_path The path where the data files can be found
#' @param scenarios the scenarios that will go into the ensemble
#' @param start A string start year
#' @param end A string end year
#' @export
#' 
ensemble<-function(data_path, scenarios, start, end) {
  gcm_scenarios<-list.dirs(data_path)
  gcm_scenarios<-gcm_scenarios[which(!grepl('ensemble',gcm_scenarios))]
  nc_file<-fileNames[1]
  # Create output directory and set it as the working directory.
  # This loop is done once for each ensemble we are creating.
  for(scenario in scenarios)
  {
    write_to<-file.path(data_path,paste('ensemble_',scenario,sep=''))
    dir.create(write_to,showWarnings=FALSE)
    setwd(write_to)
    # Try and open the file.
    tryCatch(ncid <- nc_open(file.path(gcm_scenarios[2],nc_file)), error = function(e) 
    {
      cat("An error was encountered trying to open the OPeNDAP resource."); print(e)
    })
    
    # Initialize the output NetCDF files.
    x_vals<-ncid$dim$lon$vals; y_vals<-ncid$dim$lat$vals
    li<-initialize_NetCDF(ncid, thresholds, start=start, end=end, tmax_var=FALSE, prcp_var=FALSE, x_vals, y_vals, periods=list(), t_units, p_units)
    out_filenames<-li$fileNames
    
    # Make sure the in and out filenames are the same!
    stopifnot(any(out_filenames==fileNames))
    
    # Clean up
    nc_close(ncid)
    
    # Need to loop over input gcm_scenarios for each of the derivatives. Add values to what's already in as data is read in then divide and write out at the end.
    for(file in out_filenames) {
      # Extract the file name. This is actually the variable name for this file.
      var_id<-unlist(strsplit(tail(unlist(strsplit(file,'/')),n=1),'[.]'))[1]
      input<-1
      # Open the file we will be writing to.
      ncid_out<-nc_open(file,write=TRUE)
      for(gcm_scenario_ind in 2:length(gcm_scenarios)){
        gcm_scenario<-tail(unlist(strsplit(gcm_scenarios[gcm_scenario_ind],'/')),n=1)
        if(grepl('r1i1p1', gcm_scenario) && grepl(scenario,gcm_scenario))
        {
          # Open the file we need to add to the existing stuff.
          ncid_in<-nc_open(file.path(data_path,gcm_scenario,file))
          # Get the data we need.
          var_data <- ncvar_get(ncid_in, varid=var_id)
          if (input==1) {
            ens_data<-var_data
            input<-input+1
          } else {
            ens_data<-ens_data+var_data
            input<-input+1
          }
          nc_close(ncid_in) 
        }
      }
      # Get the thresholds we need. and put them in the output file.
      ncid_in<-nc_open(file.path(data_path,gcm_scenario,file))
      ncvar_put(ncid_out,'threshold',ncvar_get(ncid_in,'threshold'))
      nc_close(ncid_in)
      # put the ensemble data in the output file.
      ens_data[is.nan(ens_data)]<--1
      ens_data<-ens_data/input
      ncvar_put(ncid_out,var_id,ens_data)
      nc_close(ncid_out)
    }
  }
}