let todoList = [
    {
        item: "Complete the developement",
        dueDate: "05-01-2025", dueTime: "01:01 AM"
    },
];

displayTodo()
function addTodo() {
    event.preventDefault();
    let todoInput = document.querySelector('#todo-input');

    let dateElement = document.querySelector('#todo-date');
    let timeElement = document.querySelector('#todo-time');


    let todoItem = todoInput.value;
    let todoDate = dateElement.value;
    let todoTime = timeElement.value;
    todoList.push({
        item: todoItem,
        dueDate: todoDate,
        dueTime: todoTime,
    },);
    todoInput.value = '';
    dateElement.value = '';
    timeElement.value = '';

    displayTodo()
}

function displayTodo() {
    let containerElement = document.querySelector('#todo-container');

    let newHtml = '';

    for (let i = 0; i < todoList.length; i++) {
        // let todoItem = todoList[i] .item;
        // let todoDate = todoList[i] .dueDate;
        // let todoTime = todoList[i] .dueTime;

        let {dueTime,dueDate,item} = todoList[i]

        newHtml += `
        <div>
        <span>${item}</span>
        <span>${dueDate}</span>
        <span>${dueTime}</span>
        <button id = "delete-button" onClick = "todoList.splice(${i},1);
        displayTodo();
        ">Delete</button>
        </div>
        `
    }
    containerElement.innerHTML = newHtml
}


// another Code
/*
let todoList = [
    {
        item: "Complete the development",
        dueDate: "05-01-2025",
        dueTime: "01:01 AM"
    },
];

displayTodo();

function addTodo() {
    event.preventDefault();

    let todoInput = document.querySelector('#todo-input');
    let dateElement = document.querySelector('#todo-date');
    let timeElement = document.querySelector('#todo-time');

    let todoItem = todoInput.value.trim();
    let todoDate = dateElement.value;
    let todoTime = timeElement.value;

    if (todoItem === "") return; // Prevent empty items

    todoList.push({
        item: todoItem,
        dueDate: todoDate,
        dueTime: todoTime,
    });

    todoInput.value = '';
    dateElement.value = '';
    timeElement.value = '';

    displayTodo();
}

function displayTodo() {
    let containerElement = document.querySelector('#todo-container');
    let newHtml = '';

    for (let i = 0; i < todoList.length; i++) {
        let { item, dueDate, dueTime } = todoList[i];

        newHtml += `
        <div class="todo-item">
            <span>${item}</span>
            <span>${dueDate}</span>
            <span>${dueTime}</span>
            <button onclick="deleteTodo(${i})">Delete</button>
        </div>
        `;
    }

    containerElement.innerHTML = newHtml;
}

function deleteTodo(index) {
    todoList.splice(index, 1);
    displayTodo();
}
*/