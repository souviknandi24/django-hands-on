# django hands on

This is repository which uses django framework to create APIs using django-rest-framework and JSON API format to send response.

This repository covers all type associations. Follow the below components for an example.

### No association (basic CRUD APIs)
`myapi > components > heroes`

Heroes APIs supports all the CRUD operations.


### One to one
_will be added soon_


### One to many
```
myapi > components > one_to_many > todos  
myapi > components > one_to_many > tasks
```

One todo can have many tasks.  

eg. Try the following APIs (include is optional, it just prefetches the associated resources)
```
/todos?include=tasks
/tasks?include=todo
```


### Many to many
```
myapi > components > many_to_many > doctors  
myapi > components > many_to_many > patients
myapi > components > many_to_many > appointments
```

One doctor can have many patients  
One patient can have many doctors   
The relationship is maintained using apppointment, each appointment belongs to one doctor and one patient.

eg. Try the following APIs (include is optional, it just prefetches the associated resources)
```
/doctors
/patients
/appointments?include=doctor,patient
```


### Polymorphic
_will be added soon_