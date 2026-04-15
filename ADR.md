# Architectural Decision Record (ADR)
## Project: Youth Case Management System

---

# ADR 1: Use Django ORM for Database Interaction

**Status:** Accepted  

## Context  
The system requires efficient interaction with the database for managing youth, cases, and rehabilitation programs.

## Alternatives Considered  
1. Raw SQL queries  
   - + More control  
   - - Harder to maintain and error-prone  

2. Django ORM  
   - + Cleaner, more readable  
   - + Secure against SQL injection  
   - - Less low-level control  

## Decision  
We chose Django ORM to handle all database interactions.

## Code Reference  
core/models.py:1–80  
core/views.py:20–40  

## Consequences  
+ Improved readability and maintainability  
+ Faster development  
- Slight limitation in complex queries  

---

# ADR 2: Use Class-Based Views (CBVs)

**Status:** Accepted  

## Context  
The application requires multiple views for listing and creating objects such as Youth and Cases.

## Alternatives Considered  
1. Function-Based Views (FBVs)  
   - + Easier for beginners  
   - - Repetitive code  

2. Class-Based Views (CBVs)  
   - + Reusable and modular  
   - + Less repetitive  

## Decision  
We selected CBVs such as ListView and CreateView.

## Code Reference  
core/views.py:1–50  

## Consequences  
+ Reduced code duplication  
+ Cleaner structure  
- Slightly more complex to understand  

---

# ADR 3: Use ForeignKey for Case–Youth Relationship

**Status:** Accepted  

## Context  
Each case must be linked to a specific youth.

## Alternatives Considered  
1. ManyToMany relationship  
   - + Flexible  
   - - Not suitable for one-to-many mapping  

2. ForeignKey  
   - + Correct representation of relationship  
   - + Simpler queries  

## Decision  
We used ForeignKey in the Case model.

## Code Reference  
core/models.py:25–40  

## Consequences  
+ Accurate data modelling  
+ Easy querying  
- Less flexibility if requirements change  

---

# ADR 4: Use ManyToMany Relationship for Rehabilitation Programs

**Status:** Accepted  

## Context  
A rehabilitation program can include multiple youth, and a youth can join multiple programs.

## Alternatives Considered  
1. ForeignKey  
   - - Does not support many-to-many  

2. ManyToManyField  
   - + Supports bidirectional relationship  

## Decision  
We used ManyToManyField in RehabilitationProgram model.

## Code Reference  
core/models.py:50–65  

## Consequences  
+ Flexible relationship modelling  
+ Efficient data linking  
- Slight complexity in queries  

---

# ADR 5: Adopt “Fat Models, Thin Views” Philosophy

**Status:** Accepted  

## Context  
Business logic should be reusable and not duplicated across views.

## Alternatives Considered  
1. Logic inside views  
   - + Quick implementation  
   - - Hard to maintain  

2. Logic inside models  
   - + Reusable  
   - + Cleaner design  

## Decision  
We placed logic inside models (e.g., is_open method).

## Code Reference  
core/models.py:40–50  

## Consequences  
+ Better maintainability  
+ Encourages OOP principles  
- Slight increase in model complexity  

---

# ADR 6: Use Single App Architecture

**Status:** Accepted  

## Context  
The project scope is relatively small and manageable.

## Alternatives Considered  
1. Multiple apps (users, cases, programs)  
   - + Scalable  
   - - More complex  

2. Single app (core)  
   - + Simpler structure  
   - + Easier integration  

## Decision  
We used a single app named "core".

## Code Reference  
Project structure  

## Consequences  
+ Easy to manage  
+ Faster development  
- May require refactoring for larger systems  

---

# ADR 7: Use Django Template System

**Status:** Accepted  

## Context  
The application requires a frontend for displaying data.

## Alternatives Considered  
1. React frontend  
   - + Modern UI  
   - - More complex setup  

2. Django templates  
   - + Integrated with backend  
   - + Faster development  

## Decision  
We used Django template system.

## Code Reference  
core/templates/core/*.html  

## Consequences  
+ Simple and efficient  
+ Tight integration with backend  
- Less dynamic compared to modern JS frameworks  

---

# ADR 8: Use QuerySet Optimization (select_related)

**Status:** Accepted  

## Context  
Displaying related objects (Case → Youth, CrimeType) may cause multiple database queries.

## Alternatives Considered  
1. Default QuerySet  
   - - Multiple queries (inefficient)  

2. Optimized QuerySet (select_related)  
   - + Reduces database hits  

## Decision  
We used select_related in CaseListView.

## Code Reference  
core/views.py:30–40  

## Consequences  
+ Improved performance  
+ Reduced database load  
- Slightly more complex query logic  

---

# ADR 9: Use Django Admin for Data Management

**Status:** Accepted  

## Context  
Admin users need a quick way to manage system data.

## Alternatives Considered  
1. Custom admin dashboard  
   - + Flexible  
   - - Time-consuming  

2. Django Admin  
   - + Built-in and powerful  
   - + Minimal setup  

## Decision  
We used Django’s built-in admin panel.

## Code Reference  
core/admin.py  

## Consequences  
+ Rapid development  
+ Easy data management  
- Limited customization compared to custom UI  

---

# ADR 10: Use ModelForms for Form Handling

**Status:** Accepted  

## Context  
Forms are required for adding Youth and Cases.

## Alternatives Considered  
1. Manual HTML forms  
   - - More code  
   - - Validation issues  

2. Django ModelForms  
   - + Automatic validation  
   - + Less code  

## Decision  
We used ModelForms.

## Code Reference  
core/forms.py  

## Consequences  
+ Faster development  
+ Built-in validation  
- Less flexibility for highly customized forms  

---