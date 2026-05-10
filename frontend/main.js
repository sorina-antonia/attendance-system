const API_BASE = "http://100.29.10.131:5000";

/* ===== LOAD STUDENTS ===== */
async function loadStudents() {
    const res = await fetch(`${API_BASE}/students`);
    const data = await res.json();

    const table = document.getElementById("students-table");
    table.innerHTML = "";

    data.forEach(s => {
        table.innerHTML += `
            <tr>
                <td>${s.student_id}</td>
                <td>${s.name}</td>
                <td>${s.email}</td>
                <td>${new Date(s.created_at).toLocaleDateString()}</td>
            </tr>
        `;
    });
}

/* ===== LOAD COURSES ===== */
async function loadCourses() {
    const res = await fetch(`${API_BASE}/courses`);
    const data = await res.json();

    const table = document.getElementById("courses-table");
    table.innerHTML = "";

    data.forEach(c => {
        table.innerHTML += `
            <tr>
                <td>${c.course_code}</td>
                <td>${c.course_name}</td>
                <td>${new Date(c.created_at).toLocaleDateString()}</td>
            </tr>
        `;
    });
}

/* ===== LOAD DROPDOWNS FOR ATTENDANCE ===== */
async function loadAttendanceForm() {
    const students = await fetch(`${API_BASE}/students`).then(r => r.json());
    const courses = await fetch(`${API_BASE}/courses`).then(r => r.json());

    const studentSelect = document.getElementById("student-select");
    const courseSelect = document.getElementById("course-select");

    students.forEach(s => {
        studentSelect.innerHTML += `<option value="${s.id}">${s.name}</option>`;
    });

    courses.forEach(c => {
        courseSelect.innerHTML += `<option value="${c.id}">${c.course_name}</option>`;
    });
}

/* ===== SUBMIT ATTENDANCE ===== */
async function submitAttendance() {
    const student_id = document.getElementById("student-select").value;
    const course_id = document.getElementById("course-select").value;
    const date = document.getElementById("date").value;
    const status = document.getElementById("status").value;

    await fetch(`${API_BASE}/attendance`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ student_id, course_id, date, status })
    });

    alert("Attendance recorded!");
}

/* ===== LOAD DASHBOARD ===== */
async function loadDashboard() {
    const res = await fetch(`${API_BASE}/attendance`);
    const data = await res.json();

    const table = document.getElementById("attendance-table");
    table.innerHTML = "";

    data.forEach(a => {
        table.innerHTML += `
            <tr>
                <td>${a.student_name}</td>
                <td>${a.course_name}</td>
                <td>${a.status}</td>
                <td>${new Date(a.date).toLocaleDateString()}</td>
            </tr>
        `;
    });
}
