import React, { Component } from "react";
import TutorialDataService from "../services/tutorial.service";


export default class AddTutorial extends Component {
  constructor(props) {
    super(props);
    this.onChangeTitle = this.onChangeTitle.bind(this);
    this.onChangeRejestracja = this.onChangeRejestracja.bind(this);
    this.onChangeDescription = this.onChangeDescription.bind(this);
    this.saveTutorial = this.saveTutorial.bind(this);
    this.newTutorial = this.newTutorial.bind(this);
    this.state = {
      id: null,
      marka: "",
      model: "",
      rejestracja: "",
      data_publikacji: "2021-01-12",
      submitted: false,
    };
  }
  onChangeRejestracja(e) {
    this.setState({
      rejestracja: e.target.value
    });
    console.log(this.state)
  }
  onChangeTitle(e) {
    this.setState({
      marka: e.target.value
    });
    console.log(this.state)
  }

  onChangeDescription(e) {
    this.setState({
      model: e.target.value
    });
  }

  saveTutorial() {
    var data = {
      marka: this.state.marka,
      model: this.state.model,
      rejestracja: this.state.rejestracja,
      data_publikacji: this.state.data_publikacji
    };

    TutorialDataService.create(data)
      .then(response => {
        this.setState({
          id: response.data.id,
          marka: response.data.title,
          model: response.data.description,
          rejestracja: response.data.rejestracja,
          data_publikacji: response.data.data_publikacji,
          submitted: true,
        });

        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
      });
  }

  newTutorial() {
    this.setState({
      id: null,
      marka: "",
      model: "",
      rejestracja: false,
      data_publikacji: "",

      submitted: false,

    });
  }


  render() {
    return (

        <div className="submit-form">
          {this.state.submitted ? (
            <div>
              <h4>You submitted successfully!</h4>
              <button className="btn btn-success" onClick={this.newTutorial}>
                Add
              </button>
            </div>
          ) : (
            <div>
            <div className="form-group">
            <label htmlFor="description">Marka</label>
            <select className="form-control" name="kategoria" id="kat" required onChange={this.onChangeTitle} defaultValue="Wybierz z listy...">
              <option disabled hidden>Wybierz z listy...</option>
              <option className="form-control" id="title" value="Audi">Audi</option>
              <option className="form-control" id="title" value="BMW">BMW</option>
              <option className="form-control" id="title" value="Mercedes">Mercedes</option>
              <option className="form-control" id="title" value="Skoda">Skoda</option>
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="title">Model</label>
            <input
              type="text"
              className="form-control"
              id="title"
              onChange={this.onChangeDescription}
            />
          </div>
          <div className="form-group">
                <label htmlFor="description">rejestracja</label>
                <input
                  type="text"
                  className="form-control"
                  id="rejestracja"
                  onChange={this.onChangeRejestracja}
                  pattern="[a-z]{2,3}+ [A-Z0-9]{4,6}$"
                />
              </div>
          <div className="imput-group date">
            <label htmlFor="data_publikacji">Data rejestracji</label>
            <input
              type="text"
              className="form-control"
              id="description"
              value='2021-01-12'
            />
          </div>
  
              <button onClick={this.saveTutorial} className="mt-5 btn btn-success">
                Submit
              </button>
            </div>
          )}
        </div>
      );
    }
  
}