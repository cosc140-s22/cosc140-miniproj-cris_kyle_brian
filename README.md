# COSC140 miniproject

## Team members

Cris, Kyle and Brian

## Miniproject descripton

For this mininproject we decided to create a small doulingo-like spanish learning website in which the user takes quizzes and receives their score back. The lessons have difficulties to them and all the questions are multiple choice. Also you have to log in after creating a super user and your grades are tracked.

## Feedback

3.7/4.0

Models and relationships look good; your model relationships are fairly complex and everything looks good for the setup.  Nicely done.

There's a problem when you leave a lesson review - if a bad value is given for stars then the view function doesn't return anything (and you get a crash).  The styling made is pretty hard to find the review button since that link was in blue and the page is pretty bright blue.

On the lesson page, if I've taken the lesson it correctly shows the score but doesn't really show what questions I've gotten right or wrong, which would have been nice.  For a lesson I haven't taken, the text "has achieved scores of" should probably be different to reflect that the user hasn't taken that quiz.

Pretty much all the view functions should have a `@login_required` decorator since all functions really require logging in.  

Overall, code structure looks pretty good; there are just some rough edges that if fixed could have improved the app quite a bit.
