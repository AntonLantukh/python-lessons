const formsUncompleted = document.querySelectorAll(".uncompleted_tasks_form");
const formsCompleted = document.querySelectorAll(".completed_tasks_form");

[...formsUncompleted, ...formsCompleted].forEach((form) => {
  console.log(form);
  form.querySelectorAll("input").forEach((el) => {
    el.addEventListener("change", () => {
      form.submit();
    });
  });
});
