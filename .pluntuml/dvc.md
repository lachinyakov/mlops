
```plantuml
actor user
database some_db_1
database some_db_2
database some_db_3
user -> some_db_1: 1. extracts data
some_db_1 -> user: returns data part 1
user -> some_db_2: 1. extracts data
some_db_2 -> user: returns data part 2
user -> some_db_3: 1. extracts data
some_db_3 -> user: returns data part 3
user -> user: 2. aggragating data to data/data.csv
user -> user: 3. index data/data.csv via dvc
user -> user: 4. index referal dvc files via git
```

1. User extracts data from several databases.
2. User aggregates all data to one large file.
   Previous steps may take a some time.

3. User indexes data/data.csv via dvc.
DVC stores information about the added file
(or a directory) in a special .dvc file
named data/data.csv.dvc
```bash

```
4. User indexes .dvc files information about data
