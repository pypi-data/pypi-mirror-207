# Django Cross-Database Field

### THIS IS AN EXPERIMENTAL PROJECT, USE AT YOUR OWN RISK

Experimental Django model field that communicates with remote (same instance Django) databases. Ideal for read-only data
fetching applications, such as fetching a user profile. 

As this is an experimental project, do your own research, try it, test it, and if you deem it good and stable enough
for your use case, adopt it. Any kind of feedback, like confirming if it works with certain versions of Django, is
greatly appreciated.

Best (or only) used with multi-database Django configurations. Check 
https://docs.djangoproject.com/en/4.2/topics/db/multi-db/ for more details.

# Getting started

1. Add `cross_database_field` to your INSTALLED_APPS.

```python
INSTALLED_APPS = [
    ...,
    'cross_database_field'
]
```

2. Import, then add the field to the desired model.

```python
from django.db import models

# Import it
from cross_database_field.fields import CrossDatabaseField, CrossDatabaseCapableModel


class YourRemoteModelInAnotherDatabase(models.Model):
    your_remote_field = models.CharField(max_length=100)

    
class YourModel(models.Model):
    your_field = models.CharField(max_length=100)
    # Use it
    cross_field = CrossDatabaseField(
        to="your_project.models.YourRemoteModelInAnotherDatabase",
        remote_db="your_remote_database"
    )

# Maybe inherit from CrossDatabaseCapableModel for extra QoL features
# Check the "Models" section below for more information about CrossDatabaseCapableModel
class YourEvenBetterModel(CrossDatabaseCapableModel):
    your_field = models.CharField(max_length=100)
    # Use it
    cross_field = CrossDatabaseField(
        to="your_project.models.YourRemoteModelInAnotherDatabase",
        remote_db="your_remote_database"
    )
```

3. Make migrations and apply them.

# Exported modules

## Fields

### `Common arguments`

These are positional arguments used by all fields listed below.

- `to` = Full path to the remote model, as a string, ex: `"your_project.models.YourRemoteModelInAnotherDatabase"`
- `remote_db` = Name of the database, as declared in Django settings file, ex: `"default"`

### `cross_database_field.fields.CrossDatabaseField`

Cross-database field for remote models with a numeric primary key. You most likely have to use this field, as the
default PK field in Django is a BigInteger.

- Remote primary key: Numeric (Any Integer type, *no decimals*)
- Locally stored as: BigInteger

### `cross_database_field.fields.UUIDCrossDatabaseField`

Cross-database field for remote models with a UUID primary key. This field is not standard, as models with a UUID PK
are uncommon, and mostly unpractical.

- Remote primary key: UUIDField
- Locally stored as: UUID if database capable, else, string or hex.

## Models

### `cross_database_field.fields.CrossDatabaseCapableModel`

Abstract model meant to be used together with cross-database fields. This abstract model is meant to simplify the
manipulation of models containing cross-database fields. This is done by allowing to circumvent some of the limitations listed above.

This model will circumvent the following limitations: 

- The first limitation, by overriding the save logic.
- The second limitation, by overriding the save logic and fetching the remote model.

To use this model, inherit from the right class in your model declaration. Like so:

```python
from django.db import models

# Import it
from cross_database_field.fields import CrossDatabaseField, CrossDatabaseCapableModel


class YourRemoteModelInAnotherDatabase(models.Model):
    your_remote_field = models.CharField(max_length=100)

    
# Inherit CrossDatabaseCapableModel instead of models.Model
class YourModel(CrossDatabaseCapableModel):
    your_field = models.CharField(max_length=100)
    cross_field = CrossDatabaseField(
        to="your_project.models.YourRemoteModelInAnotherDatabase",
        remote_db="your_remote_database"
    )
```

Keep in mind, inheriting from this model is only beneficial when your own model contains a cross-database field. Else,
it will do nothing.

# Everything else

## Usage recommendations

While the remote model contained in the cross-database field can be modified and saved independently of the original model,
this may lead to unexpected results. Make sure to test thoroughly if you're going this route.

Just as common Django models, the models contained within the cross-database fields are not guaranteed to be up-to-date.
To get the latest model representation from database, try instantiating the parent model once again.

## TODO

- Further testing of all use cases and conditions the field may be exposed to.
- Testing for Python and Django versions compatibility.
- Support deletion signals (or any other way) to handle remote model deletion.
- Write a helper tool to ease migrations to, and from, cross-database fields.

## Limitations

1. Models containing a cross-database field cannot be saved after they have been instantiated, as the cross-database 
fields will contain the remote model when instantiated. To solve this, assign the field to the PK of the containing model,
ex: `model_instance.cross_field = model_instance.cross_field.pk`
2. After dealing with the first limitation, model instances will not contain the remote model anymore, and will contain
the PK value going forward. To solve this, instantiate the field again after saving, ex:
`model_instance = YourModel.objects.get(pk=model_instance.pk)`
3. Currently, there's no way to implement remote deletion logic, such as Django's "CASCADE". When the remote model the 
cross-database field is pointing to is deleted, the field will return `None` in code instances, and will default
to empty in forms, but the database will still contain the deleted remote model PK value until saved again. Furthermore,
that means that cross-database fields will return `None` for two cases; if they're empty, or if the remote model has 
been deleted.

Check the `Exported Modules` section, `Models` subsection above for an easy way to work around some of these limitations.

## Migration

If you're using an in-house solution to fetch from remote database models, such as storing the PK of a remote model as
a value in a field, migrating to cross-database fields should be easy, as these fields store the same basic
information in the database, just as you're already doing, but provide extra business logic for ease of use.

If you're migrating away from cross-database fields, you may find the PK of the remote models in your database, as
mentioned before.

Writing, or modifying a Django migration file should be enough for both cases, and should move your data along safely.