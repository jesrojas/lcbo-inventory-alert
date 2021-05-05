import React from 'react'
import './homepage.styles.scss'

import Form from '../../components/form/form.component'

const HomePage = () => {
    return (
      <section className="hero_section">
          <Form/>
          <span className="hero_heading_mobile">LCBO</span>
          {/* <span className="hero_heading_mobile">Vigilant</span> */}
          <div className="hero_heading">
            <span className="hero_heading_letter">L</span>
            <span className="hero_heading_letter">C</span>
            <span className="hero_heading_letter">B</span>
            <span className="hero_heading_letter">O</span>
          </div>
          <div className="hero_heading_absolute">
              <span className="hero_heading_second">Vigilant</span>
          </div>
      </section>
    );
}

export default HomePage;