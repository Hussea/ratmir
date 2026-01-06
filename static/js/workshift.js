// ================== URL PARAMS ==================
const params = new URLSearchParams(window.location.search);

const employeeId = params.get("employee_id");
const projectId  = params.get("project_id");
const projectName = params.get("project_name");
const employeeName = params.get("employee_name");
const rawTime = params.get("time");
const startTimeParam = rawTime ? rawTime.substring(0, 5) : "";
const workHours = Number(params.get("time0"));

// ================== ELEMENTS ==================
const form = document.getElementById("employee-form");
const msg  = document.getElementById("form-message");

const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let photoBlob = null;

// ================== INIT ==================
if (!employeeId || !projectId) {
  msg.textContent = "Ошибка данных";
  throw new Error("Missing params");
}

document.getElementById("employee_id").value = employeeId;
document.getElementById("project_id").value = projectId;
document.getElementById("project_name").value = projectName;
document.getElementById("employee_name").value = employeeName;
document.getElementById("start_time").value = startTimeParam;

// ================== DATE LOGIC ==================
const today = new Date();
const tomorrow = new Date(today);
tomorrow.setDate(today.getDate() + 1);

const startDateInput = document.getElementById("start_date");
const endDateInput   = document.getElementById("end_date");

startDateInput.min = today.toISOString().split("T")[0];
startDateInput.max = tomorrow.toISOString().split("T")[0];

flatpickr("#end_time", {
  enableTime: false,
  noCalendar: true,
  dateFormat: "H:i",
  time_24hr: true
});

function calculateEnd() {
  if (!startDateInput.value || !startTimeParam) return;

  const start = new Date(`${startDateInput.value}T${startTimeParam}:00`);
  const end = new Date(start.getTime() + workHours * 3600000);

  endDateInput.value = end.toISOString().split("T")[0];
  document.getElementById("end_time").value =
    String(end.getHours()).padStart(2, "0") + ":" +
    String(end.getMinutes()).padStart(2, "0");
}

startDateInput.addEventListener("change", calculateEnd);

// ================== CAMERA ==================
document.getElementById("startCameraBtn").onclick = async () => {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;
    video.style.display = "block";
    document.getElementById("captureBtn").disabled = false;
  } catch {
    alert("Нет доступа к камере");
  }
};

document.getElementById("captureBtn").onclick = () => {
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;

  ctx.drawImage(video, 0, 0);

  ctx.fillStyle = "red";
  ctx.font = "20px Arial";
  ctx.fillText(`Проект: ${projectName}`, 20, 30);
  ctx.fillText(`Охранник: ${employeeName}`, 20, 60);

  canvas.toBlob(blob => {
    photoBlob = blob;
    canvas.style.display = "block";
    video.style.display = "none";
    msg.textContent = "Фото сохранено ✅";
  }, "image/jpeg", 0.9);
};

// ================== SUBMIT ==================
form.addEventListener("submit", async (e) => {
  e.preventDefault();

  if (!photoBlob) {
    msg.textContent = "Сначала сделайте фото";
    return;
  }

  const formData = new FormData(form);
  formData.append("image", photoBlob, "photo.jpg");

  const res = await fetch("/add_work_shifts", {
    method: "POST",
    body: formData
  });

  if (res.ok) {
    msg.textContent = "Отправлено успешно ✅";
      window.location.href = "/show_qr_code_fro_check_point";

  } else {
    msg.textContent = "Ошибка отправки ❌";
  }

  
});


