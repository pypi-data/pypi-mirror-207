# apininja

`apininja` is a simple CLI automation tool that generates a small boilerplate module
that serves as api for database models or other models. Currently it generates the basic
CRUD operations as well as functions for serializing a single object to dictionary.

## Sample Output

A sample output for `apininja MyModel`

```py
# API Created for my_model

def serialize_my_model(data):
	return {"id": data.id}

def serialize_my_models(lst):
	serialized = []
	for item in lst:
		serialized.append(serialize_my_model(item))
	return serialized

def my_model_list_api(lst):
	return serialize_my_models(lst)

def my_model_detail_api(data):
	return serialize_my_model(data)

def my_model_create_api(*args, **kwargs):
	pass

def my_model_update_api(*args, **kwargs):
	pass

def my_model_delete_api(*args):
	pass
```

## Installation

```py
pip install apininja
```

## Usage

```py
apininja UserModel
```
