from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('postgresql://catalog:topsecret@localhost/catalogdb')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="im Robot", email="ar.rickxxx@gmail.com")
session.add(User1)
session.commit()

# Create category of Action Films
category1 = Categories(user_id=1, name="Action Films")
session.add(category1)
session.commit()


# Create category of Adventure Films
category2 = Categories(user_id=1, name="Adventure Films")
session.add(category2)
session.commit()

# Create category of Comedy Films
category3 = Categories(user_id=1, name="Comedy Films")
session.add(category3)
session.commit()

# Create category of Crime & Gangster Films
category4 = Categories(user_id=1, name="Crime & Gangster Films")
session.add(category4)
session.commit()

# Create category of Drama Films
category5 = Categories(user_id=1, name="Drama Films")
session.add(category5)
session.commit()

# Create category of Epics/Historical Films
category6 = Categories(user_id=1, name="Epics/Historical Films")
session.add(category6)
session.commit()

# Create category of Horror Films
category7 = Categories(user_id=1, name="Horror Films")
session.add(category7)
session.commit()

# Create category of Musicals (Dance) Films
category8 = Categories(user_id=1, name="Musicals (Dance) Films")
session.add(category8)
session.commit()

# Create category of Science Fiction Films
category9 = Categories(user_id=1, name="Science Fiction Films")
session.add(category9)
session.commit()

# Create category of War (Anti-War) Films
category10 = Categories(user_id=1, name="War (Anti-War) Films")
session.add(category10)
session.commit()

# Create category of Westerns
category11 = Categories(user_id=1, name="Westerns")
session.add(category11)
session.commit()


# Add Items into categories
categoryItem1 = CategoryItem(user_id=1, name="West Side Story",
                             description="N/A",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Silence of the Lambs",
                             description="N/A",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Longest Day",
                             description="N/A",
                             categories=category10)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Apocalypse Now",
                             description="N/A",
                             categories=category10)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Scarface",
                             description="N/A",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Secret Life of Pets",
                             description="N/A",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Dance Academy: The Movie",
                             description="N/A",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Good, the Bad and the Ugly",
                             description="N/A",
                             categories=category11)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Hidden Figures",
                             description="N/A",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="300",
                             description="N/A",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Martian",
                             description="N/A",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Kingsman: The Golden Circle",
                             description="N/A",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Godfather",
                             description="N/A",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Django Unchained",
                             description="N/A",
                             categories=category11)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Dunkirk",
                             description="N/A",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Titanic",
                             description="N/A",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Star Wars: The Last Jedi",
                             description="N/A",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Deadpool",
                             description="N/A",
                             categories=category1)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1,
                             name="Pirates of the Caribbean: \
                             Dead Men Tell No Tales",
                             description="N/A",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="It",
                             description="N/A",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Despicable Me 3",
                             description="N/A",
                             categories=category3)
session.add(categoryItem1)
session.commit()

print "added category items!"
