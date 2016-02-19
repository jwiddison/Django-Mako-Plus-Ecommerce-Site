# initialize the django code
print('Initializing Django...')
import sys, os
mydir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(mydir)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Colonial_Heritage_Foundation.settings")
django.setup()

# regular imports
from account import models as amod
from catalog import models as cmod
import datetime, random, sys

#print("You should not be running this.  No soup for you.")
#sys.exit(0)

#####################################
###   Create Permissions and Groups

print()
print('Creating permissions and groups...')

# imports for permissions
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Delete all current groups
Group.objects.all().delete()


# manager group (managers have all permissions)
group_manager = Group()
group_manager.name = 'Manager'
group_manager.save()
for p in Permission.objects.all():
  group_manager.permissions.add(p)

# SalesRep group (sales reps can change only catalog items)
group_salesrep = Group()
group_salesrep.name = 'SalesRep'
group_salesrep.save()
for p in Permission.objects.filter(content_type__app_label='catalog'):
  group_salesrep.permissions.add(p)

# customer group (customers have no permissions)
group_customer = Group()
group_customer.name = 'Customer'
group_customer.save()

######################################
###   Users

print()
print('Creating users...')
amod.User.objects.all().delete()
users = []  # to save for use later
for i in range(1, 10):
  u = amod.User()
  u.username = 'user%i' % i
  u.first_name = 'First%i' % i
  u.last_name = 'Last%i' % i
  u.email = 'me%i@me.com' % i
  u.set_password('pass%i' % i)
  u.address1 = 'Address%i' % i
  u.address2 = 'Address%i' % i
  u.city = 'City%i' % i
  u.state = 'State%i' %i
  u.zip_code = 'ZipCode%i' %i
  u.birth = datetime.datetime.now()
  u.phone_number = '555-555-000%i' % i
  u.is_active = True
  if i == 1:
    u.is_staff = True
    u.is_superuser = True
  # if i == 2:
  #   u.groups.add(group_manager)
  u.save()
  print(u)
  users.append(u)
  # assign user to some groups/permissions
print('user1, pass1 is the superuser.')

# print the permissions of user2 so we know what to use with @permission_required().  user2 is in the Manager group, which has every permission.
print()
for name in sorted(users[1].get_all_permissions()):
  print('Permission:', name)


#####################################
###   Products

print()
print('Creating products...')

### NO!  Products cannot be created because they don't really exist.  Never do this:
#p = cmod.Product()

# rental items
cmod.RentalProduct.objects.all().delete()
for i in range(1, 6):
  p = cmod.RentalProduct()
  p.name = 'Rental%i' % i
  p.description = 'This rental, #%i, is a really cool rental beacuse it is number %i.' % (i, i)
  p.image = 'rental%i.png' % i
  p.status = cmod.RENTAL_STATUS_CHOICES[0][0]
  p.save()
  print(p)

# individual products
cmod.IndividualProduct.objects.all().delete()
for i in range(1, 6):
  p = cmod.IndividualProduct()
  p.name = 'IndividualProduct%i' % i
  p.description = 'This product, #%i, is an individual product.  It is a bit of a loner.' % i
  p.image = 'indprod%i.png' % i
  p.creator = random.choice(users)
  p.save()
  print(p)

# bulk products
cmod.BulkProduct.objects.all().delete()
for i in range(1, 6):
  p = cmod.BulkProduct()
  p.name = 'BulkProduct%i' % i
  p.description = 'This product, #%i, is an bulk product. It has lots of quantity.' % i
  p.image = 'bulkprod%i.png' % i
  p.quantity = random.randint(1, 100)
  p.save()
  print(p)

# Venue
venues = []  # make list to use to create events
cmod.Venue.objects.all().delete()
for i in range(1,10):
    v = cmod.Venue()
    v.name = 'Venue%i' % i
    v.address = 'Address%i' % i
    v.city = 'City%i' % i
    v.state = 'State%i' %i
    v.zip_code = 'ZipCode%i' %i
    v.save()
    venues.append(v)
    print(v)

# Events and Areas

# Delete all events and areas
cmod.Event.objects.all().delete()
cmod.Area.objects.all().delete()

for i in range(1,10):
    e = cmod.Event()
    e.name = 'Event%i' % i
    e.description = 'This event, #%i, is an event. It will be at a venue and will have areas.' % i
    e.start_date = datetime.datetime.now()
    e.end_date = datetime.datetime.now()
    e.venue = random.choice(venues)
    e.save()
    print(e)
    # Add some areas to that particular event
    for j in range(1,4):
        a = cmod.Area()
        a.name = 'Area%i' % j
        a.description = 'Description of the area %i' % j
        a.place_number = i*j
        a.event = e
        a.save()
        print(a)
