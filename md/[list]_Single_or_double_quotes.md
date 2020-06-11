# Single or Double Quotes?

__OP says:__

I am asking myself if I should preferably use single or double quotes
for strings?

If I need a single quote in a string I would use double quotes for the
whole string and vice versa. For f-strings I mostly see double
quotes but single quotes would work as well I think.

Is there a recommendation?



__ml_news at posteo.de (Manfred Lotz)__<hr>



Nothing strong. I tend to use double quotes because I have a
background in C (where double quotes are for strings, single quotes
for characters), and double quotes are the recommendation for
docstrings (see PEP 258). If you tend to work a lot with SQL, you
might prefer single quotes. Use whatever makes you happy.

__rosuav at gmail.com (Chris Angelico)__<hr>

> On Wed, May 20, 2020 at 4:21 AM Manfred Lotz <ml_news at posteo.de> wrote:
>>
>> Hi there,
>> I am asking myself if I should preferably use single or double quotes
>> for strings?
>>
>> If I need a single quote in a string I would use double quotes for the
>> whole string and vice versa. For f-strings I mostly see double
>> quotes but single quotes would work as well I think.
>>
>> Is there a recommendation?
>>
> 
> Nothing strong. I tend to use double quotes because I have a
> background in C (where double quotes are for strings, single quotes
> for characters), and double quotes are the recommendation for
> docstrings (see PEP 258). If you tend to work a lot with SQL, you
> might prefer single quotes. Use whatever makes you happy.


Have been finding myself doing somewhat the opposite:

    "a literal string"
    f'a string featuring computation of { result }'

(never managed to make it as far as C in my alphabet skills, but yes, 
maybe SQL influences)

@Chris: are you on the night-shift?

__PythonList at DancesWithMice.info (DL Neil)__<hr>
> Hi there,
> I am asking myself if I should preferably use single or double
> quotes for strings?

I'd say your consistency matters more than which one you choose.

According to a recent observation by Raymond H.


    Over time, the #python world has shown increasing preference
    for double quotes:  "hello" versus 'hello'.

    Perhaps, this is due to the persistent influence of JSON,
    PyCharm, Black, and plain English.

    In contrast, the interpreter itself prefers single quotes:

    >>> "hello"
    'hello'


[tweet](https://twitter.com/raymondh/status/1259209765072154624)

I think the worst choice is to be haphazard in your usage with a
hodgepodge of single/double quotes.

I personally use habits from my C days:  double-quotes for everything
except single characters for which I use a single-quote:

  if 'e' in "hello":

as in indicator that I'm using it as a single character rather than
as a string.

I don't have a firm rule for myself if a string contains
double-quotes.  It doesn't happen often for me in a case where I
couldn't use a triple-quoted string or that I am refering to it as a
single character.


__python.list at tim.thechases.com (Tim Chase)__<hr>

> I thought triple quotes are for docstrings?

Yes, but triple double quotes ==> """ <== not triple single quotes ==>
''' <== is what PEP 258 recommends. The description is awkward but
it's still a place where the double-quote character (U+0022 QUOTATION
MARK) is the recommendation.


> @Chris: are you on the night-shift?
Yes? :)

__rosuav at gmail.com (Chris Angelico)__<hr>

> I thought triple quotes are for docstrings?

It's the recommendation, but double and single quotes work just fine, too -- at least for docstrings that fit an one line.


__ethan at stoneleaf.us (Ethan Furman)__<hr>

I am influenced by Perl which I used before. In Perl I used double
quoted strings when I wanted interpolation. Otherwise single quoted
strings. In Rust (or C) it is double quotes for strings and single
quotes for characters. 

You may be right. Consistency is a good thing. So, I have to decide for
what I use and be consistent thereafter.


__ml_news at posteo.de (Manfred Lotz)__<hr>


And I, the shell (where single quotes are "raw" and double quotes allow 
parameter substitution).  So I use single quotes for plain old strings 
and double quotes when I'm going to be formatting the string with % 
(therefore, in most logging calls).

Personally I find double quotes visually noisy, and prefer single 
quotes. Most of the time.

This is one of the reasons I autoformat with yapf (which doesn't change 
my quoting) rather than black (which is very opinionated and also 
untunable, and _does_ change my quotes).


__cs at cskk.id.au (Cameron Simpson)__<hr>
> Hi there,
> I am asking myself if I should preferably use single or double quotes
> for strings?

Personally laziness wins every time. Single quotes only require one
finger from the home position using my right hand, double quotes
require two and a big movement of my left hand from home.

So I use single quotes most of the time (ie unless it contains
a single quote)



__alan.gauld at yahoo.co.uk (Alan Gauld)__<hr>
> Hi there,
> I am asking myself if I should preferably use single or double quotes
> for strings?
> 
> If I need a single quote in a string I would use double quotes for the
> whole string and vice versa. For f-strings I mostly see double
> quotes but single quotes would work as well I think.
> 
> Is there a recommendation?

I personally like to use "This is a phrase or sentence" while '0', '\n', 
and 'work' are items or words.

`# And this is a comment 'quoted' by '#' and '\n'.`



__tjreedy at udel.edu (Terry Reedy)__<hr>


Tim Chase <python.list at tim.thechases.com> wrote:

> On 2020-05-19 20:10, Manfred Lotz wrote:
> > Hi there,
> > I am asking myself if I should preferably use single or double
> > quotes for strings?  
> 
> I'd say your consistency matters more than which one you choose.
> 

First, thanks to all for your opinions and judgements.

I agree to the following:

1. Consistency is important.
2. Single quotes are less noisy.
3. Triple double quotes are to be preferred over triple single quotes.

I also believe that transferring habits from C, Rust or whatever to
Python doesn't make much sense as Python does not distinguish between a
character and string from a type perspective.

Of course, this is my subjective result, and others (may) have
different opinions. 



__ml_news at posteo.de (Manfred Lotz)__<hr>
>>> quotes for strings?
...

> I agree to the following:
> 
> 1. Consistency is important.
> 2. Single quotes are less noisy.
> 3. Triple double quotes are to be preferred over triple single quotes.
...

> Of course, this is my subjective result, and others (may) have
> different opinions.

4. unless a specific objective of a re-factoring exercise, maintain the 
conventions used within the code.

5, adhere to the conventions/standards/requirements of the dev.team or 
organisation.


__PythonList at DancesWithMice.info (DL Neil)__<hr>

> background in C (where double quotes are for strings, single quotes
> for characters), and double quotes are the recommendation for
> docstrings (see PEP 258). If you tend to work a lot with SQL, you
> might prefer single quotes. Use whatever makes you happy.

I also came to Python from C and tend to make the same mental distinction,
though that has softened with time. Given that I have four different
choices, I consider:

a) If it's preexisting code (especially written by someone else) I try to
maintain that style (if discernable) for consistency, subject to

b) Minimizing the need to use backslashes

I also agree about SQL. I found that something like this:

    stmt = (
        """select foo from bar"""
        """  where a = 'bag'"""
        """    and c = 'dog'"""
    )

worked pretty well, served to both satisfy my brain's desire for semantic
indentation (you should see some of the SQL I inherited - yikes!) and
maintain a visual distinction between Python and SQL quoting. (Consistently
using triple quotes minimizes the chance of needing a stray Python
backslash inside the SQL code.) I'm now retired, so can't double check, but
I believe SQLite and MSSQL are unusual in their Pythonesque treatment of
single and double quotes being synonymous. I believe most other dialects
(Oracle, MySQL, Sybase, PostgreSQL that I checked) only recognize single
quotes as string delimiters.



__skip.montanaro at gmail.com (Skip Montanaro)__<hr>
> I also believe that transferring habits from C, Rust or whatever to
> Python doesn't make much sense as Python does not distinguish between a
> character and string from a type perspective.

 From a logical perspective, you are correct.  From the point of view of 
someone who writes more C code than Python, not having to remember a new 
set of habits for Python makes life a lot simpler.

Chacun ? son go?t and all that.


__rhodri at kynesim.co.uk (Rhodri James)__<hr>

```
>>> "single or double"
'single or double'
```
I read a recent quote from Raymond Hettinger saying that the
Python world prefers double ones. If Mr Hettinger is around i'd
like to ask him where he pulled the theory from
[tweet](https://twitter.com/raymondh/status/1259209765072154624?s=20)


__arj.python at gmail.com (Abdur-Rahmaan Janhangeer)__<hr>
<arj.python at gmail.com> wrote:
>
> The interpreter prefers single-quotes
>
```
>>> "single or double"
'single or double'
```

```
>>> 'not all that strongly, it doesn\'t'
"not all that strongly, it doesn't"
```


__rosuav at gmail.com (Chris Angelico)__<hr>
> On Sat, May 23, 2020 at 10:52 PM Abdur-Rahmaan Janhangeer
> <arj.python at gmail.com> wrote:
> >
> > The interpreter prefers single-quotes
> >  
> > >>> "single or double"  
> > 'single or double'
> >  
> >>> 'not all that strongly, it doesn\'t'  
> "not all that strongly, it doesn't"

But when a string contains both, it biases towards single quotes:

    >>> "You said \"No it doesn't\""
    'You said "No it doesn\'t"'

;-)


__python.list at tim.thechases.com (Tim Chase)__<hr>

Was requoting:

> In contrast, the interpreter itself prefers single quotes:

```
>>> "hello"
'hello'
```

from R Hettinger

__arj.python at gmail.com (Abdur-Rahmaan Janhangeer)__<hr>
> I also agree about SQL. I found that something like this:

    stmt = (
         """select foo from bar"""
         """  where a = 'bag'"""
         """    and c = 'dog'"""
    )

> worked pretty well, served to both satisfy my brain's desire for semantic
> indentation (you should see some of the SQL I inherited - yikes!) and
> maintain a visual distinction between Python and SQL quoting. (Consistently
> using triple quotes minimizes the chance of needing a stray Python
> backslash inside the SQL code.) I'm now retired, so can't double check, but
> I believe SQLite and MSSQL are unusual in their Pythonesque treatment of
> single and double quotes being synonymous. I believe most other dialects
> (Oracle, MySQL, Sybase, PostgreSQL that I checked) only recognize single
> quotes as string delimiters.


The older (and more professional?) RDBMS accept either/both as variable 
delimiters, per Python strings.

My habit with SQL queries is to separate them from other code, cf the 
usual illustration of having them 'buried' within the code, immediately 
before, or even part of, the query call.

This partly because (a) some dev.teams have a specific person handling 
DBA-tasks, and partly (b) in order to make it easy to 
find/correct/re-factor SQL code without it being mixed-in with the Python.

(a) using a separate and specific module for SQL constants (which may 
include queries as text, or prepared queries), means that the 'DBA' may 
develop independently of the Python devs; that integration of code 
happens in the VCS; that the Python code may separate (stub) or 
integrate during unit-testing, according to progress and choice.

(b) physical 'extraction' and separation make it easier to develop and 
test each component (SQL, Python, ...) separately - either work in SQL 
*or* in Python, and not have the extra 'load' of having to flip one's 
brain between the two; and by using a separate module, makes it easy to 
locate a 'class' of code dealing with particular data and/or 
carrying-out particular functions - much as you might for classes and/or 
libraries.

Oh, and a further benefit: (further to "inherited", above) it becomes 
easier to avoid the massive tangles caused by trying to mix the 
conventions for indenting multi-line SQL code, with those for Python!

__PythonList at DancesWithMice.info (DL Neil)__<hr>
> On 2020-05-24 01:40, Chris Angelico wrote:
>> On Sat, May 23, 2020 at 10:52 PM Abdur-Rahmaan Janhangeer
>> <arj.python at gmail.com> wrote:
>>>
>>> The interpreter prefers single-quotes
>>>   
>>>>>> "single or double"
>>> 'single or double'
>>>   
>>>>> 'not all that strongly, it doesn\'t'
>> "not all that strongly, it doesn't"
> 
> But when a string contains both, it biases towards single quotes:
> 
>     >>> "You said \"No it doesn't\""
>     'You said "No it doesn\'t"'
> 
> ;-)


I'm highly amused by this interchange - for two reasons: that you'd 
noticed these details, and that I hadn't!

Yes, I'd noted that the REPL responds with single-quotes, even if I used 
double-quotes in the definition (per "single of double", above) - for 
whatever that's worth (it's not as if the delimiters are stored along 
with other variable detail!)

That the REPL is 'intelligent' about its choice to vary the delimiter to 
suit the content is good (design) sense - the best presentation (UX), ie 
doesn't is a better presentation than doesn\'t!

Which brings me to my own, humble, and quite often non-PEP-8-respecting 
habits: that I (basically) apply the ?rules of English grammar to Python 
(which I write (mostly) in English). Thus a "quotation", eg someone's 
name, but any piece of data, will be enclosed in double-quotes:

    name = "Abdur-Rahman"

whereas, when something will be 'calculated', I use singles, eg

    f'{ name } is top of the class'

Never learning a language which distinguishes single character literals 
from strings, eg the C examples quoted earlier, such 
thoughts/distinctions don't 'exist'.
(which makes me wonder why code reviews have never queried the point, or 
registered that I might seem to be behaving inconsistently...)

__PythonList at DancesWithMice.info (DL Neil)__<hr>
> I also agree about SQL. I found that something like this:

    stmt = (
         """select foo from bar"""
         """  where a = 'bag'"""
         """    and c = 'dog'"""
    )

> worked pretty well, served to both satisfy my brain's desire for semantic
> indentation (you should see some of the SQL I inherited - yikes!) and
> maintain a visual distinction between Python and SQL quoting. (Consistently
> using triple quotes minimizes the chance of needing a stray Python
> backslash inside the SQL code.)

May I ask why not simply like this:

stmt = """
      select foo from bar
        where a = 'bag'
          and c = 'dog'
      """

This introduces more newlines and spaces in the query, but that
shouldn't really matter. I think it's more readable, and easier to edit
the query.

> I'm now retired, so can't double check, but
> I believe SQLite and MSSQL are unusual in their Pythonesque treatment of
> single and double quotes being synonymous. I believe most other dialects
> (Oracle, MySQL, Sybase, PostgreSQL that I checked) only recognize single
> quotes as string delimiters.

Right. The SQLite developers did it that way in an effort to be
compatible with MySQL, and since have come to the realisation that that
was a mistake. In recent versions you can turn it off, in which cases
single quotes are for string literals and double quotes are for
identifiers (such as column names), as in standard SQL.
See
https://sqlite.org/quirks.html#double_quoted_string_literals_are_accepted


__roel at roelschroeven.net (Roel Schroeven)__<hr>
>
> May I ask why not simply like this:
>
> stmt = """
>       select foo from bar
>         where a = 'bag'
>           and c = 'dog'
>       """
>

Sorry, I don't recall. I wouldn't be at all surprised that it has something
to do with Emacs's Python mode behavior. Emacs wouldn't know what to do
with spaces in the string, but knows where to put string literals within
the open parens. I'm pretty sure I was doing this before triple quoted
strings existed.

Thankfully, I don't need to mess around with SQL anymore. :-)

__skip.montanaro at gmail.com (Skip Montanaro)__<hr>
>>
>>
>> May I ask why not simply like this:
>>
>> stmt = """
>>        select foo from bar
>>          where a = 'bag'
>>            and c = 'dog'
>>        """
> 
> Sorry, I don't recall. I wouldn't be at all surprised that it has something
> to do with Emacs's Python mode behavior. Emacs wouldn't know what to do
> with spaces in the string, but knows where to put string literals within
> the open parens. I'm pretty sure I was doing this before triple quoted
> strings existed.
> 
> Thankfully, I don't need to mess around with SQL anymore. :-)

Awwww. don't be like that - send it all to me, and I'll fix it for you 
(at exorbitant rates, of course)...


The above is valid - the editor has a file in one format/language, and 
is therefore applying 'the wrong rules' when it attempts to make SQL 
look like Python!


The inconvenience (cf "issue") that arises, is that many SQL debuggers 
and error-handlers (etc) will repeat-back the source-code/query 
as-provided. Consequently, those messages are all messed-up with 
extraneous tabs and new-lines, making them difficult to read and debug.
(see also: earlier post mentioning separation of languages/code)

__PythonList at DancesWithMice.info (DL Neil)__<hr>
> On Sat, 23 May 2020 11:03:09 -0500, Tim Chase
> >But when a string contains both, it biases towards single quotes:
> >  
> >   >>> "You said \"No it doesn't\""  
> >   'You said "No it doesn\'t"'  
> 
>   This is where using triple quotes (or triple apostrophes)
> around the entire thing simplifies it all... (except for a need to
> separate the four ending quotes)

Unless you're pathological. ;-)

```
>>> """I said "This contain every type of \"""Python\""" '''triple-quoted''' string, doesn't it?\""""
'I said "This contains every type of """Python""" \'\'\'triple-quoted\'\'\' string, doesn\'t it."'
```
And-you-can-quote-me-on-that'ly yers,


__python.list at tim.thechases.com (Tim Chase)__<hr>

Dennis Lee Bieber <wlfraed at ix.netcom.com> wrote:

> On Sat, 23 May 2020 11:03:09 -0500, Tim Chase
> <python.list at tim.thechases.com> declaimed the following:
> 
> 
> >
> >But when a string contains both, it biases towards single quotes:
> >  
> >   >>> "You said \"No it doesn't\""  
> >   'You said "No it doesn\'t"'  
> 
>   This is where using triple quotes (or triple apostrophes)
> around the entire thing simplifies it all... (except for a need to
> separate the four ending quotes)

Exactly, I also would opt for triple quotes in this case. 



__ml_news at posteo.de (Manfred Lotz)__<hr>

Nice idea

```
>>> '''You said "No it doesn't"'''
'You said "No it doesn\'t"'
```


__arj.python at gmail.com (Abdur-Rahmaan Janhangeer)__<hr>


>
> I'm highly amused by this interchange - for two reasons: that you'd
> noticed these details, and that I hadn't!
>

Yes Mr Chris is good for coming on with these kind of points ^^_


>
> Yes, I'd noted that the REPL responds with single-quotes, even if I used
> double-quotes in the definition (per "single of double", above) - for
> whatever that's worth (it's not as if the delimiters are stored along
> with other variable detail!)
>
> That the REPL is 'intelligent' about its choice to vary the delimiter to
> suit the content is good (design) sense - the best presentation (UX), ie
> doesn't is a better presentation than doesn\'t!
>
> Which brings me to my own, humble, and quite often non-PEP-8-respecting
> habits: that I (basically) apply the ?rules of English grammar to Python
> (which I write (mostly) in English). Thus a "quotation", eg someone's
> name, but any piece of data, will be enclosed in double-quotes:
>
>         name = "Abdur-Rahman"
>
> whereas, when something will be 'calculated', I use singles, eg
>
>         f'{ name } is top of the class'
>

This discussion dives a bit further into the philosophy
of Python.  Must reactivate the FaQ repo project.
Mr Barker is doing it for python-ideas.


__arj.python at gmail.com (Abdur-Rahmaan Janhangeer)__<hr>
> 
> My habit with SQL queries is to separate them from other code, cf the 
> usual illustration of having them 'buried' within the code, immediately 
> before, or even part of, the query call.
> 

I like that idea, as I find that I am embedding more and more SQL in my 
code.

How do you handle parameters? Do you leave placeholders ('?' or '%s') in 
the query, and leave it to the 'importer' of the query to figure out 
what is required?

__frank at chagford.com (Frank Millman)__<hr>
> On 2020-05-23 9:45 PM, DL Neil via Python-list wrote:
>>
>> My habit with SQL queries is to separate them from other code, cf the 
>> usual illustration of having them 'buried' within the code, 
>> immediately before, or even part of, the query call.
>>
> 
> I like that idea, as I find that I am embedding more and more SQL in my 
> code.
> 
> How do you handle parameters? Do you leave placeholders ('?' or '%s') in 
> the query, and leave it to the 'importer' of the query to figure out 
> what is required?


Yes. Most "connector" software includes a feature which auto-magically 
escapes all variable-data - a valuable safety feature!

I've been experimenting by going further and providing app.devs with 
functions/methods, a mini-API if you will. Given that many?most don't 
like having to deal with SQL, the extra 'insulation' boosts my personal 
popularity...
(and I need as much of that as I can get!)

__PythonList at DancesWithMice.info (DL Neil)__<hr>
> On 24/05/20 5:43 PM, Frank Millman wrote:
>> On 2020-05-23 9:45 PM, DL Neil via Python-list wrote:
>>>
>>> My habit with SQL queries is to separate them from other code, cf the 
>>> usual illustration of having them 'buried' within the code, 
>>> immediately before, or even part of, the query call.
>>>
>>
>> I like that idea, as I find that I am embedding more and more SQL in 
>> my code.
>>
>> How do you handle parameters? Do you leave placeholders ('?' or '%s') 
>> in the query, and leave it to the 'importer' of the query to figure 
>> out what is required?
> 
> 
> Yes. Most "connector" software includes a feature which auto-magically 
> escapes all variable-data - a valuable safety feature!
> 
> I've been experimenting by going further and providing app.devs with 
> functions/methods, a mini-API if you will. Given that many?most don't 
> like having to deal with SQL, the extra 'insulation' boosts my personal 
> popularity...
> (and I need as much of that as I can get!)

Ok. I will have to give it some thought.

I generate most of my SQL dynamically, constructing the query 
programmatically using the meta-data in my system.

But now I am constructing some more complex queries, which I can't 
generate automatically yet. I am hoping that a pattern emerges which I 
can use to automate them, but for now I am doing it by hand.

There are a number of parameters required, and it will not be obvious at 
first sight what values are required. If I am going to keep the queries 
in a separate module, I think that I will have to provide some sort of 
accompanying documentation with each query explaining what the required 
parameters are.

Thinking aloud, I may set up a separate module for the queries, but make 
each one a 'function', which specifies what data is required. The caller 
calls the function with the data as an argument, and the function uses 
it to build the parameter list and returns the SQL along with the 
parameters. The function can also contain documentation explaining how 
the query works.

As you say, this has the benefit of separating the SQL from the Python 
code, so I will definitely pursue this idea.

Thanks

__frank at chagford.com (Frank Millman)__<hr>

We have been talking (slightly OT for thread - apologies) about the 
narrow sub-objectives of transferring data between a Python application 
and an RDBMS. May I advise consideration of the wider specification?

For example, one may find it helpful to use a library/abstraction such 
as SQLAlchemy. Such facilitates transaction data being taken directly 
from/returned to a Python class! Whereas this discussion (above) only 
returns raw data-items, thus necessitating the application programmers 
coding an appropriate 'getter' to provide data to the RDBMS 
interface-functions, and/or a 'setter' to absorb query-results into the 
application's data-class(es)!

Of course, there are plenty of applications where one might eschew such 
advantages, eg a simple interface, and at the other end of the scale: if 
the data were to be formatted into a pandas data-frame.

Horses for courses!

__PythonList at DancesWithMice.info (DL Neil)__<hr>
