// ✅ تعريف المكون
class MyHeader extends HTMLElement {
  async connectedCallback() {
    const response = await fetch("components.html");
    const text = await response.text();

    const tempDiv = document.createElement("div");
    tempDiv.innerHTML = text;

    const template = tempDiv.querySelector("#header-template");
    const content = template.content.cloneNode(true);
    this.appendChild(content);
  }
}

customElements.define('my-header', MyHeader);

// ✅ دالة التنقل بين الصفحات
function goToPage(pageName) {
  window.location.href = pageName;
}
