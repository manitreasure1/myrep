// import Image from "next/image";
// import styles from "./page.module.css";

export default function Home() {
  return (
    <>
     <main>
      {/* Navbar */}
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container">
          <a className="navbar-brand" href="#">☕ CoffeeHouse</a>
          <div className="collapse navbar-collapse">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item"><a className="nav-link" href="#">Home</a></li>
              <li className="nav-item"><a className="nav-link" href="#menu">Menu</a></li>
              <li className="nav-item"><a className="nav-link" href="#about">About</a></li>
              <li className="nav-item"><a className="nav-link" href="#contact">Contact</a></li>
            </ul>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <section className="bg-light text-center py-5">
        <div className="container">
          <h1 className="display-4 fw-bold">Brewed Fresh, Just for You</h1>
          <p className="lead">Experience the best coffee in town.</p>
          <button className="btn btn-primary btn-lg mt-3">Order Now</button>
        </div>
      </section>

      {/* Menu */}
      <section id="menu" className="py-5">
        <div className="container">
          <h2 className="text-center mb-4">Our Favorites</h2>
          <div className="row">
            <div className="col-md-4">
              <div className="card shadow-sm">
                <div className="card-body text-center">
                  <h5 className="card-title">Cappuccino</h5>
                  <p className="card-text">Creamy and smooth, topped with foamed milk.</p>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card shadow-sm">
                <div className="card-body text-center">
                  <h5 className="card-title">Latte</h5>
                  <p className="card-text">Perfectly balanced espresso and steamed milk.</p>
                </div>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card shadow-sm">
                <div className="card-body text-center">
                  <h5 className="card-title">Espresso</h5>
                  <p className="card-text">Rich, bold, and full of flavor in every sip.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* About */}
      <section id="about" className="bg-light py-5">
        <div className="container text-center">
          <h2>About Us</h2>
          <p className="mx-auto col-md-8">
            At CoffeeHouse, we are passionate about brewing the perfect cup.
            Our beans are locally sourced and roasted with care to bring out
            the best flavors.
          </p>
        </div>
      </section>

      {/* Footer */}
      <footer id="contact" className="bg-dark text-light text-center py-4">
        <p>📍 123 Coffee Street, Accra, Ghana</p>
        <p>⏰ Open Daily: 7AM - 10PM</p>
        <p>📞 +233 000 000 0000</p>
      </footer>
    </main>
    </>
  );
}
