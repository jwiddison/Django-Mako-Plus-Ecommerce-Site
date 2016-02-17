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
  u.save()
  print(u)
  users.append(u)
  # assign user to some groups/permissions
print('user1, pass1 is the superuser.')




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
for i in range(1,6):
    v = cmod.Venue()
    v.name = 'Venue%i' % i
    v.address = 'Address%i' % i
    v.city = 'City%i' % i
    v.state = 'State%i' %i
    v.zip_code = 'ZipCode%i' %i
    v.save()
    venues.append(v)
    print(v)

# Event
events = [] # Make list to use to create areas
cmod.Event.objects.all().delete()
for i in range(1,6):
    e = cmod.Event()
    e.name = 'Event%i' % i
    e.description = 'This event, #%i, is an event. It will be at a venue and will have areas.' % i
    e.start_date = datetime.datetime.now()
    e.end_date = datetime.datetime.now()
    e.venue = random.choice(venues)
    e.save()
    events.append(e)
    print(e)


# Area
cmod.Area.objects.all().delete()
for i in range(1,6):
    a = cmod.Area()
    a.name = 'Area%i' % i
    a.description = 'This area, #%i, is an area.  It is at an Event.' % i
    a.place_number = 'Place%i' % i
    a.event = random.choice(events)
    a.save()
    print(a)
