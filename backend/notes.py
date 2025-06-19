from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
import os

router = APIRouter()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["magic_notes"]
notes_col = db["notes"]

class Note(BaseModel):
    email: str
    content: str

class NoteUpdate(BaseModel):
    note_id: str
    content: str

class NoteDelete(BaseModel):
    note_id: str

@router.post("/note/add")
def add_note(note: Note):
    result = notes_col.insert_one({"email": note.email, "content": note.content})
    return {"note_id": str(result.inserted_id)}

@router.post("/note/update")
def update_note(note: NoteUpdate):
    result = notes_col.update_one({"_id": ObjectId(note.note_id)}, {"$set": {"content": note.content}})
    if result.matched_count:
        return {"message": "Note updated"}
    raise HTTPException(status_code=404, detail="Note not found")

@router.post("/note/delete")
def delete_note(note: NoteDelete):
    result = notes_col.delete_one({"_id": ObjectId(note.note_id)})
    if result.deleted_count:
        return {"message": "Note deleted"}
    raise HTTPException(status_code=404, detail="Note not found")

@router.get("/note/list")
def list_notes(email: str):
    notes = list(notes_col.find({"email": email}))
    return [{"note_id": str(n["_id"]), "content": n["content"]} for n in notes]