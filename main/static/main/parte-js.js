document.addEventListener("DOMContentLoaded", function() {
  /* ========================================
     FAQ Toggle
  ======================================== */
  const faqBoxes = document.querySelectorAll('.faq-box');
  faqBoxes.forEach(box => {
    const title = box.querySelector('.faq-title');
    if (title) {
      title.addEventListener('click', () => {
        const content = box.querySelector('.faq-text');
        const icon = box.querySelector('.faq-arrow');
        if (content.style.display === 'block') {
          content.style.display = 'none';
          if (icon) {
            icon.classList.remove('fa-chevron-up');
            icon.classList.add('fa-chevron-down');
          }
        } else {
          content.style.display = 'block';
          if (icon) {
            icon.classList.remove('fa-chevron-down');
            icon.classList.add('fa-chevron-up');
          }
        }
      });
    }
  });

  /* ========================================
     Pricing Table Toggle
  ======================================== */
  const pricingButtons = document.querySelectorAll('.button-selector a');
  const basicTable = document.getElementById('basic-table');
  const proTable = document.getElementById('pro-table');
  const vipTable = document.getElementById('vip-table');

  function hideAllTables() {
    if (basicTable) basicTable.style.display = 'none';
    if (proTable) proTable.style.display = 'none';
    if (vipTable) vipTable.style.display = 'none';
  }

  // Si existe la tabla básica, se muestra inicialmente
  if (basicTable) {
    hideAllTables();
    basicTable.style.display = 'table';
  }

  // Listener para los botones de planes
  pricingButtons.forEach(btn => {
    btn.addEventListener('click', function(e) {
      e.preventDefault();
      // Quita la clase "button-selected" de todos
      pricingButtons.forEach(b => b.classList.remove('button-selected'));
      // Añade la clase al botón actual
      this.classList.add('button-selected');

      // Oculta todas las tablas y muestra la correspondiente
      hideAllTables();
      if (this.id === 'basic-btn' && basicTable) {
        basicTable.style.display = 'table';
      } else if (this.id === 'pro-btn' && proTable) {
        proTable.style.display = 'table';
      } else if (this.id === 'vip-btn' && vipTable) {
        vipTable.style.display = 'table';
      }
    });
  });

 

  /* ========================================
     Scroll interno en index.html
  ======================================== */
  // Verifica si estamos en index.html o en raíz "/"
  const isIndex = window.location.href.includes("index.html") ||
                  (window.location.pathname.endsWith("/") || window.location.pathname.endsWith("\\"));
  const menuLinks = document.querySelectorAll('.menu-link');

  menuLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const targetId = link.getAttribute('data-target');
      if (isIndex && targetId) {
        // Previene navegación y hace scroll suave
        e.preventDefault();
        const section = document.getElementById(targetId);
        if (section) {
          window.scrollTo({
            top: section.offsetTop - 70, // Ajusta el offset si tu navbar es fixed
            behavior: 'smooth'
          });
        }
      } else if (targetId) {
        // Si NO estamos en index, redirige con ancla
        link.href = `index.html#${targetId}`;
      }
    });
  });

  
});
