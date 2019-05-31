from google.cloud import scheduler_v1beta1
client = scheduler_v1beta1.CloudSchedulerClient()
#project_id resembles to the project in which you are working upon in google cloud
#location is the location in which your google account services are located
parent = client.location_path(project_id, location)
#job object contains all the information required to run the job.
job = {
	"name": "projects/{project_id}/locations/{location}/jobs/{job_name}",
	"schedule":"* * * * *", #Cron syntax to run the job
	"pubsub_target":{
		"topic_name":"projects/{project_id}/topics/{topic_name}",
		"data":{message}
	}
};
response = client.create_job(parent, job)
