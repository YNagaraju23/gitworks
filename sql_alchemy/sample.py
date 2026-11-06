from sqlalchemy import (create_engine, MetaData, table, column, Integer, String)
engine = create_engine('postgresql+psycopg://root:root@localhost:5432/people', echo=True)
print(engine)


#creating Alchemy style
metadata=MetaData()
employees=table("employee",metadata, column("id", Integer, primary_key=True),column("name", String(100)))
metadata.create_all(engine)

#ORM base
class employee(Base):
    __table__="employee"
    id:map[Integer]
    name:map[String]
    salary:map[Integer]


Employees=[(id=101,name="ravi"),(id=102,name="ramu")]

#
with session(engine) as session:
    session.add_all(employees)
    session.commit()








with session(engine) as session:
    stmt=session.select(Employees)
    result=session.execute(stmt)
    employees=result.scalars.all()
