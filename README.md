# CDC-Wonder-MCD

This program is a commnad line query tool that uses CDC Wonder's API to access and retrieve records from the Multiple Cause of Death (MCD) database. This program was adapted from [alipphardt's](https://github.com/alipphardt) fantastic work on the CDC Wonder API for Single Cause of Death (SCD) database located here: https://github.com/alipphardt/cdc-wonder-api and was modified to query the MCD database and allow for options not allowed in the SCD query. Specifically, D77.V13 which allows for selection of MCD ICD-10 codes and D77.V2 which allows for selection of underlying cause of death ICD-10 codes. 

This program is reliant on the [requests](https://pypi.org/project/requests/) library.

In the current state, the program selections are optimized for one branch of our current study (deaths with all underlying causes) but can be modified accordingly. Currently the program asks for year range (in the form of the ranges described in the study), gender, and race (in the form of the groups used in the study) but these can easily be functionalized or modified such as to allow for automation or create dictionaries to allow for different year ranges or combinations of gender or race in order to suit different further studies. The output of the program currently is set to the XML request sent to CDC Wonder API for error checking and the raw XML data. We have left the raw XML output in order to allow for increased modularity as different studies may require different parsing solutions (Excel, SAS, SPSS, R).

Further documentation of the CDC WONDER API can be found at [CDC Wonder's API documentation](https://wonder.cdc.gov/wonder/help/wonder-api.html).

Additionally, more detailed documentation of the parameters as well as examples of possible parsing and graphing solutions can be found at [alipphardt's SCD repo](https://github.com/alipphardt/cdc-wonder-api).
