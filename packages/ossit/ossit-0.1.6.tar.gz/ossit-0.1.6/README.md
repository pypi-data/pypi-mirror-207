# Ossit

- API helper to connect to Ossi's API.

## Usage

### Authentication

- Configure your domain key in the ossit module.

```python
import ossit
ossit.domain_key = 'Your-Own-Unique-Domain-Key-That-Secure'
```

### Domain
```python
import ossit
# Retries domain information
domain_data = ossit.Domain.get_deaitls()
```

### Data

Data groups are used to help store related statistics. Data must belong to a group. 

```python
import ossit
# Retries data group information
data_group_data = ossit.Group.get_deaitls()
group_list = ossit.Group.get_list()

# Enter data into a group.
data = ossit.Data().enter(
    group_name='Revenue',
    data_name='BBQ Sales',
    data_value=1000,
    method_type='set'
)
```