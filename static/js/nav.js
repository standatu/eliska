document.addEventListener('DOMContentLoaded', function() {
  const navToggle = document.querySelector('.nav-toggle');
  const mobileNavModal = document.querySelector('.mobile-nav-modal');
  const closeNavModal = document.querySelector('.close-modal');

  // Funkce pro přepínání modálního navigačního menu
  function toggleModal() {
      mobileNavModal.classList.toggle('active');
  }

  // Otevření modálního menu
  navToggle.addEventListener('click', toggleModal);

  // Zavření modálního menu
  closeNavModal.addEventListener('click', toggleModal);

  // Zavření modálního menu kliknutím mimo menu
  window.addEventListener('click', function(event) {
      if (event.target === mobileNavModal) {
          toggleModal();
      }
  });

  // Optional: Zavření modálního menu na stisk klávesy Esc
  window.addEventListener('keydown', function(event) {
      if (event.key === 'Escape') {
          if (mobileNavModal.classList.contains('active')) {
              toggleModal();
          }
      }
  });

  // Optional: Ovládání podpoložek navigace
  // Toto je pouze ukázka, může vyžadovat úpravy podle vaší konkrétní implementace
  document.querySelectorAll('.nav-menu > li > a').forEach(function(menuItem) {
      menuItem.addEventListener('click', function(event) {
          let dropdown = menuItem.nextElementSibling;
          if (dropdown && dropdown.classList.contains('dropdown')) {
              event.preventDefault(); // Zabrání navigaci odkazu, pokud existují podpoložky
              dropdown.classList.toggle('active');
          }
      });
  });
});
