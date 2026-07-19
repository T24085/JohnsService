import './styles.css'
import './responsive-overrides.css'
import './section-polish.css'
import './motion-pass.css'

const image = (name) => `${import.meta.env.BASE_URL}images/${name}`
const phone = 'tel:+17852634444'
const facebook = 'https://www.facebook.com/profile.php?id=100036158832105'
const maps = 'https://www.google.com/maps/search/?api=1&query=425+N+Buckeye+Ave+Abilene+KS+67410'
const year = new Date().getFullYear()

document.querySelector('#app').innerHTML = `
  <a class="skip-link" href="#main-content">Skip to content</a>
  <header class="site-header" data-header>
    <a class="brand" href="#top" aria-label="John's Service home">
      <span class="brand-mark" aria-hidden="true"><span>J</span><i>24/7</i></span>
      <span class="brand-name"><strong>John's</strong><small>Service</small></span>
    </a>
    <nav class="desktop-nav" aria-label="Primary navigation">
      <a href="#services">Services</a>
      <a href="#fleet">Our fleet</a>
      <a href="#about">Why John's</a>
      <a href="#location">Find us</a>
    </nav>
    <a class="header-phone" href="${phone}"><span class="phone-dot" aria-hidden="true"></span> Call 785 263 4444 <b aria-hidden="true">↗</b></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="mobile-menu"><span>Menu</span><i aria-hidden="true"></i></button>
    <div class="mobile-menu" id="mobile-menu">
      <span class="menu-kicker">John's Service · Abilene, KS</span>
      <a href="#services">Services <span>01</span></a>
      <a href="#fleet">Our fleet <span>02</span></a>
      <a href="#about">Why John's <span>03</span></a>
      <a href="#location">Find us <span>04</span></a>
      <a href="#contact">Get help now <span>↗</span></a>
      <a class="mobile-call" href="${phone}">Call 785 263 4444</a>
      <p>425 N Buckeye Ave<br />Abilene, Kansas 67410</p>
    </div>
  </header>

  <main id="main-content">
    <section class="hero" id="top">
      <div class="hero-photo"><img src="${image('flag-night.jpg')}" alt="John's Service heavy recovery truck outside the Abilene station at dusk" /></div>
      <div class="hero-scrim" aria-hidden="true"></div>
      <div class="hero-grid">
        <div class="hero-kicker reveal"><span class="status-dot"></span> Always open · Central Kansas</div>
        <div class="hero-copy reveal reveal-delay">
          <p class="eyebrow">Towing · Recovery · Repair</p>
          <h1>When the road<br /><em>stops.</em> We don't.</h1>
          <p class="hero-lede">Light-duty roadside help and heavy-duty recovery, backed by a local crew that knows how to get things moving again.</p>
          <div class="hero-actions"><a class="button button-yellow" href="${phone}">Call for help <span>↗</span></a><a class="text-link light-link" href="#services">See what we do <span>↓</span></a></div>
        </div>
        <div class="hero-facts reveal reveal-delay-2"><span><b>24/7</b><small>Response</small></span><i></i><span><b>785</b><small>263-4444</small></span><i></i><span><b>KS</b><small>Based local</small></span></div>
      </div>
      <div class="hero-scroll"><span>Scroll to explore</span><i>↓</i></div>
      <div class="hero-number" aria-hidden="true">01</div>
    </section>

    <section class="intro section-pad" id="about">
      <div class="section-label reveal"><span>01</span><i></i><span>The John's standard</span></div>
      <div class="intro-grid">
        <div class="intro-title reveal"><p class="eyebrow">Local when it matters most</p><h2>Built for the<br /><em>long haul.</em></h2></div>
        <div class="intro-copy reveal reveal-delay"><p>John's Service is the call to make when a bad day needs a capable answer. From roadside assistance in town to heavy recovery beyond it, the work is straightforward: show up, handle the situation, and help you get on with your day.</p><a class="text-link" href="#contact">Start with a call <span>↗</span></a></div>
      </div>
      <div class="intro-media reveal"><img src="${image('dinosaur-sign.jpg')}" alt="The green dinosaur landmark above the John's Service station" /><div class="media-caption"><span>Abilene, Kansas</span><span>Home base since day one</span></div></div>
    </section>

    <section class="services section-pad dark-section" id="services">
      <div class="section-label section-label-light reveal"><span>02</span><i></i><span>What we handle</span></div>
      <div class="services-heading reveal"><p class="eyebrow eyebrow-yellow">One number. More capability.</p><h2>Ready for the<br /><em>unexpected.</em></h2><p>Practical help for drivers, fleets, and the people waiting on the other side of a breakdown.</p></div>
      <div class="service-list">
        <article class="service-card reveal"><span class="service-index">01</span><div><h3>Light-duty towing</h3><p>Safe, dependable towing for cars, pickups, and everyday roadside calls.</p></div><span class="service-arrow">↗</span></article>
        <article class="service-card reveal reveal-delay"><span class="service-index">02</span><div><h3>Heavy-duty recovery</h3><p>Serious equipment and experienced handling for trucks, trailers, and demanding recoveries.</p></div><span class="service-arrow">↗</span></article>
        <article class="service-card reveal reveal-delay-2"><span class="service-index">03</span><div><h3>Roadside & lockouts</h3><p>Jump starts, lockouts, roadside support, and the quick response you need to keep moving.</p></div><span class="service-arrow">↗</span></article>
        <article class="service-card reveal"><span class="service-index">04</span><div><h3>Auto repair</h3><p>Local shop support when the vehicle needs more than a tow to get back on the road.</p></div><span class="service-arrow">↗</span></article>
      </div>
    </section>

    <section class="fleet section-pad" id="fleet">
      <div class="fleet-heading reveal"><div class="section-label"><span>03</span><i></i><span>Working equipment</span></div><p class="eyebrow">The fleet behind the phone number</p><h2>Big enough for<br /><em>the hard jobs.</em></h2></div>
      <div class="fleet-gallery">
        <button class="gallery-image gallery-large reveal" type="button" data-lightbox="${image('blue-wrecker.jpg')}" data-alt="Blue heavy-duty John's Service wrecker truck"><img src="${image('blue-wrecker.jpg')}" alt="Blue heavy-duty John's Service wrecker truck" /><span>Heavy recovery <b>↗</b></span></button>
        <button class="gallery-image gallery-tall reveal reveal-delay" type="button" data-lightbox="${image('heavy-duty-recovery.webp')}" data-alt="John's Service truck assisting a semi"><img src="${image('heavy-duty-recovery.webp')}" alt="John's Service truck assisting a semi" /><span>On the road <b>↗</b></span></button>
        <button class="gallery-image gallery-wide reveal reveal-delay-2" type="button" data-lightbox="${image('white-flatbed-close.jpg')}" data-alt="White John's Service flatbed tow truck"><img src="${image('white-flatbed-close.jpg')}" alt="White John's Service flatbed tow truck" /><span>Flatbed service <b>↗</b></span></button>
      </div>
      <div class="fleet-note reveal"><span>01 — 03</span><p>From local flatbeds to heavy recovery equipment, the right truck changes the outcome.</p></div>
    </section>

    <section class="statement" aria-label="John's Service statement"><div class="statement-image"><img src="${image('long-haul-recovery.webp')}" alt="A tractor-trailer on a rural Kansas road" /></div><div class="statement-overlay"></div><div class="statement-copy reveal"><p class="eyebrow eyebrow-yellow">For the miles ahead</p><p class="statement-line">Good help<br />travels <em>far.</em></p><a class="button button-yellow" href="${phone}">Talk to the team <span>↗</span></a></div><div class="statement-testimonials reveal reveal-delay-2" data-testimonial-rail><div class="testimonial-heading"><span>Customer notes</span><span class="testimonial-count"><b data-testimonial-count>01</b> / 03</span></div><div class="testimonial-rating" aria-label="4.9 out of 5 stars"><span aria-hidden="true">★★★★★</span><small>4.9 / 5 public rating</small></div><div class="testimonial-slides"><article class="testimonial-slide is-active" data-testimonial-slide><p>“They woke up very early to help me out of the ditch — and charged a fair price.”</p><small>Public customer review</small></article><article class="testimonial-slide" data-testimonial-slide><p>“They arrived across town in under 10 minutes and had the truck unlocked right away.”</p><small>Public customer review</small></article><article class="testimonial-slide" data-testimonial-slide><p>“From towing to fixing, the service was top notch.”</p><small>Public customer review</small></article></div><div class="testimonial-controls"><button type="button" data-testimonial-prev aria-label="Previous testimonial">←</button><span class="testimonial-progress"><i data-testimonial-progress></i></span><button type="button" data-testimonial-next aria-label="Next testimonial">→</button></div></div><div class="statement-word" aria-hidden="true">JOHN'S</div></section>

    <section class="location section-pad" id="location">
      <div class="location-heading reveal"><div class="section-label"><span>04</span><i></i><span>Find us</span></div><h2>Right where<br /><em>you need us.</em></h2><div class="location-details"><p>John's Service<br />425 N Buckeye Ave<br />Abilene, Kansas 67410</p><a class="button button-yellow" href="${maps}" target="_blank" rel="noopener noreferrer">Get directions <span>↗</span></a></div></div>
      <div class="map-frame reveal reveal-delay"><iframe title="Google map showing John's Service in Abilene, Kansas" src="https://www.google.com/maps?q=425+N+Buckeye+Ave,+Abilene,+KS+67410&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe><div class="map-badge"><span class="status-dot"></span><div><strong>John's Service</strong><small>425 N Buckeye Ave · Abilene, KS</small></div><a href="${maps}" target="_blank" rel="noopener noreferrer">Open in Google Maps <span>↗</span></a></div></div>
    </section>

    <section class="contact section-pad dark-section" id="contact">
      <div class="contact-grid">
        <div class="contact-copy reveal"><div class="section-label section-label-light"><span>05</span><i></i><span>Get in touch</span></div><p class="eyebrow eyebrow-yellow">Don't wait on the shoulder</p><h2>Let's get you<br /><em>moving.</em></h2><p class="contact-lede">Call anytime. We’ll get the right person and the right equipment headed your way.</p><div class="contact-details"><a class="contact-phone" href="${phone}">(785) 263-4444 <span>↗</span></a><a href="${maps}" target="_blank" rel="noopener noreferrer">425 N Buckeye Ave · Abilene, KS <span>↗</span></a><span>Always open · Central Kansas</span><a href="${facebook}" target="_blank" rel="noopener noreferrer">Follow John's Service on Facebook <span>↗</span></a></div></div>
        <form class="help-form reveal reveal-delay" data-help-form><div class="form-heading"><span>Prefer to send a note?</span><small>We’ll follow up as soon as possible.</small></div><label for="name">Name</label><input id="name" name="name" type="text" autocomplete="name" placeholder="Your name" required /><label for="phone-input">Phone</label><input id="phone-input" name="phone" type="tel" autocomplete="tel" placeholder="Best number to reach you" required /><label for="need">What do you need?</label><textarea id="need" name="need" rows="4" placeholder="Tell us where you are and what happened."></textarea><button class="button button-yellow" type="submit">Request a call <span>↗</span></button><p class="form-status" data-form-status role="status"></p></form>
      </div>
    </section>
  </main>

  <footer class="site-footer"><a class="brand" href="#top"><span class="brand-mark" aria-hidden="true"><span>J</span><i>24/7</i></span><span class="brand-name"><strong>John's</strong><small>Service</small></span></a><p>Light & heavy-duty towing<br />Abilene, Kansas</p><div class="footer-links"><a href="${facebook}" target="_blank" rel="noopener noreferrer">Facebook ↗</a><a href="#top">Back to top ↑</a><small>© ${year} John's Service</small></div></footer>
  <div class="lightbox" data-lightbox-modal aria-hidden="true"><button type="button" class="lightbox-close" data-lightbox-close aria-label="Close image">×</button><img data-lightbox-image alt="" /><p data-lightbox-caption></p></div>
`

window.requestAnimationFrame(() => document.body.classList.add('is-ready'))

const header = document.querySelector('[data-header]')
const menuToggle = document.querySelector('.menu-toggle')
const mobileMenu = document.querySelector('#mobile-menu')
const closeMenu = () => { menuToggle.setAttribute('aria-expanded', 'false'); mobileMenu.classList.remove('is-open'); document.body.classList.remove('menu-open') }
menuToggle.addEventListener('click', () => { const open = menuToggle.getAttribute('aria-expanded') !== 'true'; menuToggle.setAttribute('aria-expanded', String(open)); mobileMenu.classList.toggle('is-open', open); document.body.classList.toggle('menu-open', open) })
mobileMenu.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu))
window.addEventListener('scroll', () => header.classList.toggle('is-scrolled', window.scrollY > 28), { passive: true })

const observer = new IntersectionObserver((entries) => entries.forEach((entry) => entry.target.classList.toggle('is-visible', entry.isIntersecting)), { threshold: 0.12 })
document.querySelectorAll('.reveal').forEach((element) => observer.observe(element))

const testimonialRail = document.querySelector('[data-testimonial-rail]')
const testimonialSlides = [...document.querySelectorAll('[data-testimonial-slide]')]
const testimonialCount = document.querySelector('[data-testimonial-count]')
const testimonialProgress = document.querySelector('[data-testimonial-progress]')
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)')
let testimonialIndex = 0
let testimonialTimer

const showTestimonial = (nextIndex) => {
  testimonialIndex = (nextIndex + testimonialSlides.length) % testimonialSlides.length
  testimonialSlides.forEach((slide, index) => slide.classList.toggle('is-active', index === testimonialIndex))
  testimonialCount.textContent = String(testimonialIndex + 1).padStart(2, '0')
  testimonialProgress.style.transform = `scaleX(${(testimonialIndex + 1) / testimonialSlides.length})`
}

const stopTestimonialTimer = () => window.clearInterval(testimonialTimer)
const startTestimonialTimer = () => {
  stopTestimonialTimer()
  if (reducedMotion.matches) return
  testimonialTimer = window.setInterval(() => showTestimonial(testimonialIndex + 1), 6000)
}

testimonialRail.querySelector('[data-testimonial-prev]').addEventListener('click', () => { showTestimonial(testimonialIndex - 1); startTestimonialTimer() })
testimonialRail.querySelector('[data-testimonial-next]').addEventListener('click', () => { showTestimonial(testimonialIndex + 1); startTestimonialTimer() })
testimonialRail.addEventListener('mouseenter', stopTestimonialTimer)
testimonialRail.addEventListener('mouseleave', startTestimonialTimer)
testimonialRail.addEventListener('focusin', stopTestimonialTimer)
testimonialRail.addEventListener('focusout', (event) => { if (!testimonialRail.contains(event.relatedTarget)) startTestimonialTimer() })
reducedMotion.addEventListener('change', startTestimonialTimer)
showTestimonial(0)
startTestimonialTimer()

const modal = document.querySelector('[data-lightbox-modal]')
const modalImage = modal.querySelector('[data-lightbox-image]')
const modalCaption = modal.querySelector('[data-lightbox-caption]')
const closeLightbox = () => { modal.classList.remove('is-open'); modal.setAttribute('aria-hidden', 'true'); document.body.classList.remove('lightbox-open') }
document.querySelectorAll('[data-lightbox]').forEach((button) => button.addEventListener('click', () => { modalImage.src = button.dataset.lightbox; modalImage.alt = button.dataset.alt; modalCaption.textContent = button.dataset.alt; modal.classList.add('is-open'); modal.setAttribute('aria-hidden', 'false'); document.body.classList.add('lightbox-open') }))
modal.querySelector('[data-lightbox-close]').addEventListener('click', closeLightbox)
modal.addEventListener('click', (event) => { if (event.target === modal) closeLightbox() })
document.addEventListener('keydown', (event) => { if (event.key === 'Escape') { closeLightbox(); closeMenu() } })

document.querySelector('[data-help-form]').addEventListener('submit', (event) => { event.preventDefault(); const form = event.currentTarget; const firstName = form.elements.name.value.trim().split(' ')[0]; const status = form.querySelector('[data-form-status]'); status.textContent = `Thanks${firstName ? `, ${firstName}` : ''}. We’ll be in touch soon.`; status.classList.add('is-visible'); form.reset() })
