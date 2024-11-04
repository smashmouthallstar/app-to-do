let todoList = [
    "Demo Task 1",
    "Demo Task 2"
];

const listElement = document.getElementById("list")
const addButton = document.getElementById("addbtn")
const deleteButton = document.getElementById("deletebtn")

function updateTasks() { 
    listElement.innerHTML = ""; 
    for (let i = 0; i < todoList.length; i++) {
        let newTaskElement = document.createElement("li"); //Create <li> element
        newTaskElement.textContent = todoList[i]; // Add text to li element
        listElement.appendChild(newTaskElement);
    }
} //adds everything, so to fix, tell JS to clear list every update

function addTask(taskName) {
    todoList.push(taskName) //append equivalent in python
    updateTasks();
}

function deleteTask() {
    todoList.pop()
    updateTasks();
}

addButton.addEventListener("click", () => {
    const task =  prompt("Enter task name")
    addTask(task)
}) //html has certain events called at the moment of interaction. (i.e. click event)


deleteButton.addEventListener("click", () => {
    deleteTask()
})

updateTasks();

console.log(listElement);


