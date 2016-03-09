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
# imports for permissions
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
# other useful imports
import datetime, random, sys


##UNCOMMENT these lines when finished
#print("You should not be running this on a production system.")
#sys.exit(0)

#####################################
###   Create Permissions and Groups
print()
print('Creating permissions and groups...')

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
  if i == 2:
    u.save()
    u.groups.clear()
    u.user_permissions.clear()
    u.groups.add(group_manager)
  if i== 3:
    u.save()
    u.groups.clear()
    u.user_permissions.clear()
    u.groups.add(group_salesrep)
  if i== 4:
    u.save()
    u.groups.clear()
    u.user_permissions.clear()
    u.groups.add(group_customer)
  u.save()
  print(u)
  users.append(u)
  # assign user to some groups/permissions
print('user1, pass1 is the superuser.')

# print the permissions of user2 so we know what to use with @permission_required().  user2 is in the Manager group, which has every permission.
print()
print('These are all the permissions:')
for name in sorted(users[1].get_all_permissions()):
    print('Permission:', name)


#####################################
###   Categories

print()
print('Creating Categories...')

cmod.Category.objects.all().delete()
categories=[]
for i in range(1,4):
    c = cmod.Category()
    c.name = 'Category%i' % i
    c.description = 'This is category %i.' % i
    c.save()
    print(c)
    categories.append(c)


#####################################
###   Products

print()
print('Creating products...')

#####################################
###   Getting pictures ready to randomly load up products

# get the possible items from the images directory
item_names = [ ( os.path.splitext(os.path.split(name)[1])[0].replace('_', ' ').title(), os.path.split(name)[1] ) for name in glob.glob(os.path.join(mydir, 'catalog/media/pics/*.jpg')) ]
random.shuffle(item_names)
item_iterator = itertools.cycle(item_names)
lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


# rental items
cmod.RentalProduct.objects.all().delete()
for i in range(1, 10):
    p = cmod.RentalProduct()
    p.name = 'Rental%i' % i
    p.price = '$100.00'
    p.description = 'This is rental product #%i. It has a status.' % i
    p.image = 'rental%i.png' % i
    p.category = random.choice(categories)
    p.status = cmod.RENTAL_STATUS_CHOICES[0][0]
    p.purchase_date = datetime.datetime.now()
    p.save()
    print(p)

# individual products
cmod.IndividualProduct.objects.all().delete()
for i in range(1, 10):
    p = cmod.IndividualProduct()
    p.name = 'IndProd%i' % i
    p.price = '$50.00'
    p.description = 'This is individual product #%i.  It has a creator.' % i
    p.image = 'indprod%i.png' % i
    p.category = random.choice(categories)
    p.creator = random.choice(users)
    p.create_date = datetime.datetime.now()
    p.save()
    print(p)

# bulk products
cmod.BulkProduct.objects.all().delete()
for i in range(1, 10):
    p = cmod.BulkProduct()
    p.name = 'BulkProd%i' % i
    p.price = '$5.00'
    p.description = 'This is bulk product, #%i. It has a quantity.' % i
    p.image = 'bulkprod%i.png' % i
    p.category = random.choice(categories)
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
    e.description = 'This is event #%i. It will be at a venue and will have areas.' % i
    e.start_date = datetime.datetime.now()
    e.end_date = datetime.datetime.now()
    e.venue = random.choice(venues)
    e.save()
    print(e)
    # Add some areas to that particular event
    for j in range(1,4):
        a = cmod.Area()
        a.name = 'Area%i' % j
        a.description = 'Description of area %i' % j
        a.place_number = i*j
        a.event = e
        a.save()
        print(a)
