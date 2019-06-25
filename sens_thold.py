#sum of the database and return whether that sum is greater than a certain threshold
def query(db, thresold=5):
  return (db.sum()>thresold).float()

db, pdbs = create_db_and_parallel(10)
db.sum()

#output return the value in 0 or 1 
db.sum()>5

query(db)
#the database 10 times and calculate the sensitivity each time
for i in range(10):
  sen_f=sensitivity(query,n_enteries=10)
  print(sen_f)




