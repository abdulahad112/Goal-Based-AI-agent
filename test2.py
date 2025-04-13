import streamlit as st
import random

class Environment:
    def __init__(self, rows, cols):
        self.grid = [['Dirty' if random.random() < 0.5 else 'Clean' for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def is_dirty(self, x, y):
        return self.grid[x][y] == 'Dirty'

    def clean(self, x, y):
        self.grid[x][y] = 'Clean'

    def get_grid(self):
        return self.grid


class GoalBasedAgent:
    def __init__(self, env):
        self.env = env

    def goal(self):
        for i in range(self.env.rows):
            for j in range(self.env.cols):
                if self.env.is_dirty(i, j):
                    return True
        return False

    def perceive_and_act(self):
        actions = []
        for i in range(self.env.rows):
            for j in range(self.env.cols):
                if self.env.is_dirty(i, j):
                    self.env.clean(i, j)
                    actions.append(f"Tile ({i},{j}) was Dirty. Cleaned.")
                else:
                    actions.append(f"Tile ({i},{j}) was already Clean.")
        return actions


# Streamlit App
st.set_page_config(page_title="Goal-Based Vacuum Cleaner", layout="centered")

st.title("🧹 Goal-Based Vacuum Cleaner Agent")

rows = st.slider("Select number of rows", 2, 10, 3)
cols = st.slider("Select number of columns", 2, 10, 3)

if st.button("Start Cleaning"):
    env = Environment(rows, cols)
    agent = GoalBasedAgent(env)

    st.subheader("🔹 Initial Room State")
    st.table(env.get_grid())

    if agent.goal():
        actions = agent.perceive_and_act()
        st.subheader("🧠 Agent Actions")
        for action in actions:
            st.write(action)

        st.subheader("✅ Final Room State")
        st.table(env.get_grid())
        st.success("Goal Achieved: All tiles are clean!")
    else:
        st.info("Room is already clean!")
