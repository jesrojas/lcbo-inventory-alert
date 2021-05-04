import React from 'react';
import './form.styles.scss';

import { CustomButton } from '../custom-button/custom-button.component'

const Form = () => (
  <div className="alert_form">
      <p className="form_heading">Find your bottle</p>
      <p className="form_paragraph">
        LCBO Vigilant keeps a watch on the LCBO Website to make sure you always
        get an alert when an item gets back in stock. At the moment, this is only
        a prototype that works with emails. Make sure you insert the item’s URL.
      </p>
      <form>
        <input type="email" placeholder="Email" className="form-input" />
        <input type="url" placeholder="URL" className="form-input" />
        <CustomButton type="submit">Sign me up</CustomButton>
      </form>
  </div>
);

export default Form;