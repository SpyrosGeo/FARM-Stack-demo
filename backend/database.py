from model import Todo

#mongodb Driver
import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://thatguy:1248@farmstack.dpgah.mongodb.net/test?authSource=admin&replicaSet=atlas-ftve5e-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true') 


db = client.TodoList
collection = db.todo


async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title,description):
    await collection.update_one({"title":title},{"$set":{
        "description":description
    }})
    document = await collection.find_one({"title":title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True