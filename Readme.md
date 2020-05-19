# django hands on

This is repository which uses django framework to create APIs using django-rest-framework and JSON API format to send response.

This repository covers all type associations. Follow the below components for an example.

### No association (basic CRUD APIs)
`myapi > components > heroes`

Heroes APIs supports all the CRUD operations.


### One to one
_will be added soon_


### One to many
`myapi > components > todos`  
`myapi > components > tasks`

One todo can have many tasks.  

eg. Try the following APIs (include is optional, it just prefetches the associated resources)
```
/todos?include=tasks
/tasks?include=todo
```

Heroes APIs supports all the CRUD operations.  


### Many to many
_will be added soon_


### Polymorphic
_will be added soon_