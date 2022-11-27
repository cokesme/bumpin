# Azure

## Issues 
Had to turn on a bunch of settings for the subscription and if even if a resource manager for a group wants to do something
these settings already need to be on.

* Microsoft.Web for Azure Function
* Microsoft.EventGrid for hooking function up to storage account?
* Microsoft.Insights for seeing what is going on with Logic App

## Connecting logic App
* need to build out some perms
* then need to go back to storage account if new function and create a connection thing again
* then go to logic app and look at overview and see trigger history to get the api to put in the connection thing
* logic functions need to come in as a webhook for somme reason? and not an azure function? 

This shit makes me so sad:
how the world to have to know the length of the subject in the body of this api upload? 
`split(triggerBody()?['subject'], '/')?[7]`
Why can I not index from the end [-1], plz