import streamlit as st
import operations as op


todos = op.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    existing_todos = op.get_todos()
    existing_todos.append(new_todo)
    op.put_todos(existing_todos)

st.title("My TODO application")
st.subheader("Todos")
st.write("This app will increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input("",placeholder= "Enter your new TODO here",
              on_change=add_todo, key="new_todo")