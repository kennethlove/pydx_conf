# Teach a New Object Old Tricks

Hi, I'm Kenneth. I work for Treehouse, where I teach pretty much anything that
relates to Python. I've also been a Python user for quite awhile.

So, I'm expecting you to ask me questions. Interrupt me. I have a lot I want to
cover but, in the end, it's more important that you all understand this stuff
than that I check off every box. Also, follow along with me. I'm gonna give you
some challenges as we go, too.

## Python 3

I'll be using Python 3 for all of this. Specifically, Python 3.5. If you only
have Python 2, that's fine. You'll just have to type an extra thing or two. I'll
try to point those out but, again, interrupt me if I forget.

## What does OO mean?
### Design pattern

Object-oriented programming, or OO, or OOP, is a way to program.
It's a design pattern, which is a fancy jargon way of saying that it's a common,
repeatable way to organize your code and approach problems. Programming is
really just problem solving so OO is a way to solve problems in the greater
scheme of programming. It's not *the* way, it's not even *the best* way, but
it's a way and, for most people and most problems, it's a really *good* way.

### Especially handy for real-world concepts

This is especially true when we're dealing with real-world concepts. Taking a
bunch of data and filtering it down, like finding all of the men's shoes that
are between $15 and $65 isn't really a "real world" thing. It's just some work
to do. Probably not a good thing to solve with OO.

*But*, talking about a shoe, or a store, or a transaction, any of these things
are definitely handled well by object-oriented programming. You can make a store
object or a shoe object and then do *stuff* with it. Anything you can think of
as "I want to do stuff to this thing" is usually a good candidate for OO.

### Everything in Python is an object already

And, in the world of Python, everything is an object. Every variable you make,
every function, every...everything. Everything is an object so, once you get
used to objects and OO, Python starts to make a bit more sense and be a bit more
predictable.

## What is an object?

### Objects are generally nouns

So what is an object? Object is a programming construct that has attributes and
methods. Hold onto those words, we'll come back to them. Objects are *usually*
nouns. They're *things*. Like I said before, a shoe, a store, a transaction.
*Things*. Nouns.

You can definitely have objects that represent verbs or adjectives but those are
usually a little trickier to keep in your mental map. They don't fit as nicely
with my next few analogies, either.

### Objects have attributes

OK, let's go back. I said that objects have attributes. How many of you know
what I mean if I say "namespace"?

A namespace is a group of names. Like, in your family, you have names that mean
a particular person. Maybe it's "mom" or "dad" or "Jake" or something. In that
space, your family, the name "Anne" means a particular person. In your work or
school namespace, though, "Anne" might be a completely different person.

In Python, it's pretty much the same thing. In one file, the variable `age`
might be 35 and in another one it might be 27. Even inside of that file, the
`age` variable in the outermost scope, or the global scope, might be one value
but inside of a function, it could be a different one. The function has its own
namespace.

Objects have their own namespace, too. Any variables that are just floating
around in this namespace are called "attributes". Attributes are like, well, the
attributes of your object. So if we go back to a shoe, the attributes would be
the color, the size, the brand, the model, the lace color and length, and so on.
These are kind of the adjectives that describe your object.

### Objects also have methods

And, in that class' namespace, you can have functions. We call these functions
"methods", though, so that we can distinguish them from functions that are just
hanging out in some module or namespace.

Methods always, until I tell you different in a few minutes, affect the instance
that you're currently working with. Oh, hey, this is a good time for some code.

```python
class Shoe:
    size = 9.5
    color = "red"

    def put_on(self):
        print("You put on your {} shoes.".format(self.color))
```

So we have a class, Shoe, and it has two attributes and one method. This is one
of those places, Python 2 users, that you'll need to do something extra. You'll
need to add `(object)` after your class name and before the colon. In Python 2,
we still had these weird Python 1 classes hanging around and you have to
explicitly tell Python to use "new style" classes by extending `object`. Oops,
there's another word we won't get to for a bit: extending. Sorry, file that one
away again.

### self

What's this first argument to `put_on`, though? This `self` thing? Most of the
time, when we use a class, we make an instance of it. Instances are kind of like
copies of a class. When you use the `list()` function, or the list literal `[]`,
you're creating an instance of the list class. So to make an instance of our
class, we call it like it's a function.

```python
my_shoes = Shoe()
```

And now I have access to its attributes.

```python
my_shoes.color
"red"
my_shoes.size
9.5
```

And I have access to its methods.

```python
my_shoes.put_on()
"You put on your red shoes."
```

Each instance can have its own attributes, too. Let's change the color of my
shoes.

```python
my_shoes.color = "blue"
```

And then use the method again.

```python
my_shoes.put_on()
"You put on your blue shoes."
```

Awesome! New shoe color. I wish it was actually that easy.

### Class attributes vs instance attributes

But...here's a weird thing. Let's make another Shoe instance.

```python
your_shoes = Shoe()
```

If we check the color, they should be red.

```python
your_shoes.color
"red"
```

Cool. Exactly what we expected. Maybe I want Shoe to have a black shoe by
default though. At least, in this process. I'm not going to change the class
definition, this but that starts with `class`, I'm just going to change the
class.

```python
Shoe.color = "black"
```

Let's check the your shoes are still red.

```python
your_shoes.color
"black"
```

What?! Oh, right. We never *explicitly* set the color of your shoes. So, when an
instance hasn't had a value set explicitly, and you ask for it, Python just goes
back to the class to find out what it should be. That's easier than putting
every value on every instance of the class. But, in this case, we changed the
class later and got a value we didn't expect. Something good to keep in mind and
something we can, and will, fix later.

## classmethod
In Python, we have these things called "decorators". They're bits of code,
usually functions, that can take another bit of code and apply some behavior to
it. Maybe you want to be able to mark a function as only being callable by
someone with the proper credentials, an admin or something. You could write a
decorator that checks that person's credentials before it lets the function run.
You'd do this as decorator instead of just some code you write paste into the
function because, chances are, you want to do this to a lot of functions.

I say all of that to say, this next thing we're gonna talk about, uses a
decorator.

So, every method in a class runs on an instance of the class, right? Well, not
exactly. I mean, by default, yes. But we can make methods that don't need an
instance to run and just work on their own class. Usually we use these to make
special methods for creating new instances of a class.

Let's make one so that we can just describe our shoes to create our new instance
with the size and color that we want.

```python
@classmethod
def create(cls, description):
    shoe = cls()
    size, color = description.split()
    shoe.size = float(size)
    shoe.color = color
    return shoe
```

The `@classmethod` decorator tells Python that this method should get the class
instead of an instance of the class. And, our first argument, is `cls` which
we'll just know means "the class". You could use any other variable you wanted,
of course, but you probably want to avoid "self" and you can't use "class".

So, then, inside, we use the class that's provided to the method to make a new
instance of it. Then we split the description on the space and assign the values
back to the instance that we made.

Let's see if it works.

```python
new_shoes = Shoe.create("10.5 orange")
print(new_shoes.size)
new_shoes.put_on()
```

Awesome, works a treat.

## staticmethod

The other special type of method that we should learn about is the static
method. A static method doesn't care about an instance or a class. It's just a
method that belongs to a class because it makes sense for that method to belong
to that class. I don't find myself, personally, using these a lot, but they are
handy in certain cases.

Let's make a static method that'll take a list of shoe descriptions and gives us
back all of the shoes.

```python
@staticmethod
def shoe_rack(shoes):
    for shoe in shoes:
        yield Shoe.create(shoe)
```

So this method just takes a single argument. It could very well be a function
that we just include in the module. It makes *sense*, though, to keep it with
the class. 

## What is inheritance?

OK, so we've seen a lot about creating brand new classes, but what about if we
don't want to make all of our class functionality ourselves? What if we want, I
dunno, a class that behaves like a string but has some special new thing. This
is where inheritance comes in.

It's like your genes, your DNA. One or more classes go in, and a new class comes
out. OK, so, it's kinda hard for you to only have one set of genes, but bear
with me. Let's not jump to making new lists or anything just yet. Let's start
with a new base class.

```python
class Monster:
    sound = "Rarrr!"

    def attack(self):
        print("The monster cries '{}' and attacks!".format(self.sound))

    def give_up(self):
        print("The monster throws down its weapons and runs away!")
```

Let's make a second monster type, too, that inherits from `Monster`. We'll make
a troll.

```python
class Troll(Monster):
    sound = "Well, actually..."

    def give_up(self):
        print("The troll yells 'Never!' and calls in Twitter reinforcements!")
```

Obviously trolls well-actually everyone, right? OK, but what if our troll has a
new attribute that our monster doesn't have? We should know whether or not our
troll has a bridge.

```python
class Troll(Monster):
    sound = "Well, actually..."
    bridge = False
```

By default, we won't give trolls a bridge. Most are still living at home under
their parents' bridge. But now we get a fun thing where we can't check the
bridge-y-ness of our regular monsters because they don't have that attribute.

```python
monster = Monster()
troll = Troll()

print(troll.bridge)
print(monster.bridge)
```

Oh no! `AttributeError`! As you probably guessed, classes don't have attributes
that we don't give to them. Your parent classes won't automatically inherit the
attributes of their child classes. Child classes, though, *do* get all of the
attributes of their parent classes. Again, it's a DNA thing. That's why we can
still do

```python
troll.attack()
```

And when we do

```python
troll.give_up()
```

We don't get the monster version, we get the troll version. We can't even easily
get to the monster version from a troll instance.

### super()
OK, so what about something where the parent class has it and the child class
wants to use it but wants to use it a little differently? I'm pretty sure trolls
don't attack exactly like just plain old monsters do.

```python
class Troll(Monster):
    def attack(self):
        print("The troll says something mean about you.")
        super().attack()
```

Now, if we make our troll attack, we'll get a different message *before* we get
the regular message. The `super()` there tells Python to go look at the parent
class and use its version of the method. Handy when you need to just change some
little part and not the entire thing.

If you're using Python 2, you'll need to do your `super()` a little differently.
It'll need to be `super(Troll, self).attack()`. In Python2, we have to specify
the class name and then either an instance of the class or a type that's a
subclass of the class you gave. Python 3's version is a lot simpler.


## Magic methods

In the title, I said "teach a new object old tricks". What I meant by that was,
originally, just making your objects extend and/or act like built in objects.
But then I decided I should do it all from the ground up so, yay, finally to the
bit I originally had planned!

Python objects have a bunch of methods known as "magic methods". They're magic
because you, the average, every day progammer, never really call them but they
get used all the time. They get used when you make a new object or when you ask
for a member by index or all sorts of other things. All of the magic methods
look the same; they all start and end with two underscores. If you have a really
good imagination, it *kind of* looks like a magician's top hat.

Let's start with the one you'll most commonly overwrite, init.

### __init__

Init is run whenever a new instance of a class has been created. There's
actually another method, new, that's run *before* init, but you won't modify it
nearly as often.

Remember how we had the problem of our shoes not having a solid size or color
until we set them on the instance itself? Let's fix that.

```python
class Shoe:
    def __init__(self, size=9.5, color='red'):
        self.size = size
        self.color = color
```

init doesn't need to ever return anything. In fact, if you do return something
other than `None`, you'll get a `TypeError`. 

Now let's check our shoe stuff again.

```python
my_shoes = Shoe()
Shoe.color = 'blue'
print(my_shoes.color)
```

Ha ha, take that, Python!

Init is your best entry point when you need to customize the creation of an
instance. Whether you want to set attributes or start other processes or
whatever, this is the place to start.

### __str__ and __repr__

Another really common magic method is str. Str controls how your instance
becomes a string. In Python 2, by the way, you have to be a bit more careful of
this because strings can't hold unicode characters. You'll probably want a magic
unicode method, too. One more headache solved by Python 3.

```python
class Shoe:
    def __str__(self):
        return '{}, size {}'.format(self.color, self.size)
```

And now

```python
print(str(my_shoes))
```

Now we have to do that `str()` conversion. If we just print it, we'll get the
representation of the object which usually includes its memory address and stuff
like that.

```python
print(my_shoes)
```

That's controlled by another method, `__repr__`, but I'll leave that one for you
to explore. You can also control how objects become ints, floats, and booleans
but the ideas there are pretty much the same as for `__str__`, so, again, I'll
leave them for you.

### __add__ and __radd__ and __iadd__

So maybe your object already is a number or knows how to become a number. Let's,
uh, let's set up a new class, `Song`.

```python
class Song:
    title = None
    artist = None
    total_seconds = 0

    def __init__(self, title=None, artist=None, time='00:00:00'):
        self.title = title
        self.artist = artist
        self.time = time
        self.total_seconds = self.__set_total_seconds(time)
```

Now this double underscore before `set_total_seconds` makes it so we can *only*
call this method from within this class, a subclass, or an instance. This is
pretty much the only way to protect a method in Python.

```python
def __set_total_seconds(self, time):
    if time.count(':') != 2:
        raise ValueError(
            "'time' argument should only be hours:minutes:seconds."
        )
    seconds, minutes, hours = map(int, time.split(':')[::-1])
    seconds += minutes * 60
    seconds += hours * 3600
    return seconds
```

OK, so, we make sure the time argument is in the right format, then we break it
apart on the colons, reverse the list, and turn each bit into an int. Then, to
figure out the total number of seconds, we do some math on each bit.

Now let's add a method to turn a song into an int.

```python
def __int__(self):
    return self.total_seconds
```

OK, but we can't add two songs together just yet. We have number versions of
them but they don't know how to add yet. Let's try it, though, just to be sure.

```python
song1 = Song(time='00:00:10')
song2 = Song(time='00:01:00')
print(song1+song2)
```

And, yep, TypeError. The operands, the two songs on the side, don't know how to
add themselves together. We can fix that with two methods.

First, let's set up the `__add__` method. This method is for the item on the
left side of the plus sign.

```python
def __add__(self, other):
    return self.total_seconds + other
```

Well, that didn't fix it. And the problem is that the object on the *right* side
of the plus sign doesn't know how to add itself to something on the left side.
They both have the `__add__` method but to add yourself to something when you're
on the right side, you actually need a new method, `__radd__`. No, the "r"
doesn't stand for "right", it stands for "reflected". Python actually tries
to swap the operands around when it fails on `__add__` and that's where we get
"reflected" from.

```python
def __radd__(self, other):
    return self.total_seconds + other
```

Yes, we wrote exactly the same code. That won't *always* be the case, but it
seems to be *most* of the time. You could totally just have `__radd__` return
`self.__add__(self, other)` but that seems messy and easy to forget about.

Anyway, if we run our check now, it passes.

```python
song1 = Song(time='00:00:10')
song2 = Song(time='00:01:00')
print(song1+song2)
```

Yep, there's our 70 we were expecting.

If you want to be able to change the value on the left in place, like when you
do `x += 1`, you'll want to override a method named `__iadd__`, for "in-place
add". You'll also look at overriding methods like `__mul__`, `__sub__`, and
`__div__`, for controlling multiplication, subtraction, and division. Each of
them has an `r` equivalent, too.

### __getitem__

So, we've made objects into strings and numbers and made them addable. What if
we want our object to act like a list or a dictionary? Let's go back to our
monsters. And, by the way, this is a really iffy example. I'm not sure why you'd
ever do this this way.

```python
class Monster:
    def __init__(self, sound='Rarr!', left_hand=None, right_hand=None):
        self.sound = sound
        self.left_hand = left_hand
        self.right_hand = right_hand

    def __getitem__(self, key):
        try:
            return self.__dict__[key]
        except KeyError as err:
            raise err
```

Every time you set at attribute or method on an object, Python actually updates
an internal dictionary on the object. Everything is stored as keys and values in
a dictionary and you can get to that dictionary through an attribute named
`__dict__`. So, basically, we're just making our attributes work like dictionary
keys here. It's like having JavaScript objects in Python.

Anyway, if we use it, it should work.

```python
monster = Monster(left_hand='axe')
print(monster['left_hand'])
```

Yeah, there's our 'axe' value.

You can also override `__getitem__` to work with numbers, indexes, so that your
class behaves like a list, tuple, or string. Again, I like to give you things to
explore on your own. You probably want to look at `__contains__`, too.

### __iter__

If we want our custom class to be something that we can iterate over, something
we can use in a loop, we have to define the `__iter__` method. This method has
to return a new iterator that can iterate over all of the items in the class.
Or, well, all of the things you *want* to iterate over. Our monsters are sad,
they don't have a home. Let's give them a dungeon.

```python
import random

class Dungeon:
    trouble = []

    def __init__(self, monsters=None):
        if monsters:
            self.trouble.extend(monsters)

    def __iter__(self):
        random.shuffle(self.trouble)
        return (m for m in self.trouble)
```

So first we shuffle the list of trouble, the list of monsters, and then we
return a generator expression of all of the monsters in there. We could return a
list comprehension or a new list or whatever would be most appropriate. Using a
generator here gives us a bit of niceness, though, in case we have a really
large dungeon or our monsters get a bit hefty in memory consumption.

```python
m1 = Monster()
m2 = Monster(sound='Urk!')
t1 = Troll()
t2 = Troll(sound='Discrimination is a fairy tale!')

dungeon = Dungeon(monsters=[m1, m2, t1, t2])
print(list(dungeon))
```

And there's two monsters and two trolls.

If you want a challenge, go add an `__add__` method to the `Dungeon` class so
that you can add monsters in later.

### __call__

I have one last magic method I want to talk about. We use `str()` and `list()`
all the time in Python to make strings and lists and ints and whatever. But each
of these is actually a class, too.

Let's make a somewhat contrived example to illustrate this. Let's make a class
that lets us quickly do addition with a base number.

```python
class Add:
    def __init__(self, default=0):
        print("init")
        self.default = default

    def __call__(self, extra=0):
        print("call")
        return self.default + extra
```

This is a weird one to get your head around the first time, at least for me.

When we instantiate an instance of this class, we'll give it a default value, or
0, that it'll always add to everything. Then, when we call an instance of it,
we'll add whatever value it's called with, or 0 again, to the default value.

```python
add5 = Add(5)
print(add5(5))
print(add5(12))
```

So now we have an instance that we can call like it's a function and pass an
argument to. This is a little weird, yes, but it *can* come in very handy,
especially when you have a class that needs to be an action item.

## Properties

So we know how to make new objects. We know how to do inheritance. And we know
how to do emulation. There's one more major part of object-oriented programming
that we haven't talked about and that's "encapsulation". Or, to take it out of
the realm of jargon, controlling access to bits and pieces. One of the major
ways people do encapsulation in Python is with properties.

A property is an object method that acts like an attribute. It's for calculated
things, most of the time. 

### Getters

In a new module, I'm going to make a new class named `Person`.

```python
import datetime


class Person:
    def __init__(self, name, birth_date=None):
        self.name = name
        self.birth_date = birth_date

    @property
    def days_alive(self):
        return (datetime.datetime.today - birth_date).days
```

So we're going to assume that we always get a `datetime` as a birth date. We
should probably add some checks into this but we can do that later.

```python
me = Person(name='Kenneth', birth_date=datetime.datetime(1981, 5, 16))
me.days_alive
```

So, there we go, a property that calculates the number of days someone has been
alive.

### Setters

But properties are a one-way street. They only give us information back out.
What if we want to be able to calculate something, like days alive or play time
or something, but we *also* want to be able to update it, or at least the
information it uses to make its calculation, too? And, because we're nice
programmers, we want to use the same attribute name. No reason to make people
learn different names for getters and setters, right? Lookin' at you, Java.

Let's start by updating our `Song` class.

```python
class Song:
    def __init__(self, title=None, artist=None, time='00:00:00'):
        self.__total_seconds = 0

    @property
    def total_seconds(self):
        return self.__total_seconds
```

So, for now, that's just going to return 0 every time. Not exactly the most
handy thing ever, huh? We need to provide a way to update the total time
at instance creation and whenever we want after that.

Let's add a setter for this property.

```python
@total_seconds.setter
def total_seconds(self, time):
    if time.count(':') != 2:
        raise ValueError(
            "'time' argument should only be hours:minutes:seconds"
        )
    seconds, minutes, hours = map(int, time.split(':')[::-1])
    seconds += minutes * 60
    seconds += hours * 3600
    self.__total_seconds = seconds
```

Let's ignore the `@total_seconds.setter` decorator for now. This method is our
old `__set_total_seconds` method. But, at the end, instead of returning our
`seconds` that we calculated, we're setting them back onto the instance. So,
now, assuming our `total_seconds` attribute gets updated somewhere, we should
have a valid time. Let's try it.

```python
song = Song(time='00:00:10')
print(song.total_seconds)
```

Hmm, still 0. What if we update it?

```python
song.total_seconds = '00:00:10'
print(song.total_seconds)
```

Alright, we got 10. Awesome. OK, now to roll that all into one because I don't
want to have to do that double setting over and over again.

```python
class Song:
    def __init__(self, title=None, artist=None, time='00:00:00'):
        self.title = title
        self.artist = artist
        self.time = time
        self.__total_seconds = 0
        self.total_seconds = time
```

Ah, so now we set the `__total_seconds` attribute *and* the `total_seconds`
property in the `__init__` method. That way we have a default, baseline amount
of time, 0 seconds, but then we update it with our property setter.

```python
song = Song(time='00:00:30')
song.total_seconds
```

Yeah, there we go, works just like we expected.

## Wrap up

You'll find yourself using some of these things more often than others. You'll
use inheritance quite often, most likely. You'll use `__init__` all the time.
You'll make `@property`s way more often than you'll make the setters for them.

Python's OO is pretty friendly. It has great docs and everything works pretty
much like you'd expect it to. There are some things I didn't talk about, but you
should look them up later on if you want to learn more about OO or you find some
particularly tricky problem you need to solve. Those things are: descriptors;
the MRO, or method resolution order; and extending Python's built-in objects.
All three of these things are less common than the stuff we went over today,
though, so it may be a long time before you run into any of them...or you might
*never* run into them.

## Questions?
