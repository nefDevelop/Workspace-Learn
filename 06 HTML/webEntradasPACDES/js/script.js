const init = () => {
    const submitBtn = document.querySelector("#submitBtn");
    const terms = document.querySelector("#terms");
    const form = document.querySelector("#form");
  
    handlerTermsBtn(terms, submitBtn);
    handlerFormData(form);
  };
  
  const handlerTermsBtn = (terms, submitBtn) => {
    terms.addEventListener("click", () => {
      if (terms.checked) {
        submitBtn.classList.add("activeBtn");
        submitBtn.disabled = false;
      } else {
        submitBtn.classList.remove("activeBtn");
        submitBtn.disabled = true;
      }
    });
  };
  
  const handlerFormData = (form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
  
      const formData = new FormData(form);
  
      const resp = {
        name: formData.get("name"),
        date: formData.get("date"),
        place: formData.get("place"),
        tickets: formData.get("tickets"),
        category: formData.get("category"),
        paymentMethod: formData.get("payment"),
      };
  
      sessionStorage.setItem("formData", JSON.stringify(resp));
      window.location.href = "/confirmacion.html";
    });
  };
  
  const getSessionData = () => {
    const data = JSON.parse(sessionStorage.getItem("formData"));
  
    if (!data) {
      window.location.href = "./index.html";
    }
  
    if (data) {
      document.querySelector("#name").textContent = data.name;
      document.querySelector("#date").textContent = data.date;
      document.querySelector("#place").textContent = data.place;
      document.querySelector("#tickets").textContent = data.tickets;
      document.querySelector("#category").textContent = data.category;
      document.querySelector("#paymentMethod").textContent = data.paymentMethod;
    }
  };
  
  const getCurrentYear = (span) => {
    const currentYear = new Date().getFullYear();
    span.textContent = currentYear;
  };
  
  document.addEventListener("DOMContentLoaded", () => {
    const url = window.location.pathname;
    const spanYear = document.querySelector('#year');
  
    if (url === "/confirmacion.html") getSessionData();
    else init();
  
    getCurrentYear(spanYear);
  });
  