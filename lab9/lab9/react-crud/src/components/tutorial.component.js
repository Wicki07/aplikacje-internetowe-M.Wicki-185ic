import React, { Component } from "react";
import TutorialDataService from "../services/tutorial.service";

export default class Tutorial extends Component {
  constructor(props) {
    super(props);
    this.onChangeTitle = this.onChangeTitle.bind(this);
    this.onChangeDescription = this.onChangeDescription.bind(this);
    this.onChangeRejestracja = this.onChangeRejestracja.bind(this);
    this.getTutorial = this.getTutorial.bind(this);
    this.updatePublished = this.updatePublished.bind(this);
    this.updateTutorial = this.updateTutorial.bind(this);
    this.deleteTutorial = this.deleteTutorial.bind(this);
    this.state = {
      currentTutorial: {
        id: null,
        marka: "",
        model: "",
        rejestracja: false,
        data_publikacji: "",

      },
      message: ""
    };
  }

 
  componentDidMount() {
    this.getTutorial(this.props.match.params.id);
  }

  onChangeTitle(e) {
    const title = e.target.value;
    console.log(title)
    this.setState(prevState => ({
      currentTutorial: {
        ...prevState.currentTutorial,
        marka: title
      }
    }));
  }

  onChangeDescription(e) {
    const description = e.target.value;
    this.setState(prevState => ({
      currentTutorial: {
        ...prevState.currentTutorial,
        model: description
      }
    }));
  }
  onChangeRejestracja(e) {
    const description = e.target.value;
    
    this.setState(prevState => ({
      currentTutorial: {
        ...prevState.currentTutorial,
        rejestracja: description
      }
    }));
  }

  getTutorial(id) {
    TutorialDataService.get(id)
      .then(response => {
        this.setState({
          currentTutorial: response.data
        });
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
      });
  }

  updatePublished(status) {
    var data = {
      id: this.state.currentTutorial.id,
      title: this.state.currentTutorial.title,
      description: this.state.currentTutorial.description,
      data_publikacji: this.state.currentTutorial.data_publikacji,
      published: status
    };

    TutorialDataService.update(this.state.currentTutorial.id, data)
      .then(response => {
        this.setState(prevState => ({
          currentTutorial: {
            ...prevState.currentTutorial,
            published: status
          }
        }));
        console.log(response.data);
      })
      .catch(e => {
        console.log(e);
      });
  }

  updateTutorial() {
    TutorialDataService.update(
      this.state.currentTutorial.id,
      this.state.currentTutorial
    )
      .then(response => {
        console.log(response.data);
        this.setState({
          message: "Tutorial został dodany!"
        });
      })
      .catch(e => {
        console.log(e);
      });
  }

  deleteTutorial() {    
    TutorialDataService.delete(this.state.currentTutorial.id)
      .then(response => {
        console.log(response.data);
        this.props.history.push('/tutorials')
      })
      .catch(e => {
        console.log(e);
      });
  }

  render() {
    const { currentTutorial } = this.state;

    return (
      <div>
        {currentTutorial ? (
          <div className="edit-form">
            <h4>Pojazd</h4>
            <form>

              <div className="form-group">
                <label htmlFor="description">Marka</label>
                <select class="form-control" name="kategoria" id="kat" required onChange={this.onChangeTitle}>
   					      <option disabled selected hidden>Wybierz z listy...</option>
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
                  value={currentTutorial.model}
                  onChange={this.onChangeDescription}
                />
              </div>
              <div className="form-group">
                <label htmlFor="description">rejestracja</label>
                <input
                  type="text"
                  className="form-control"
                  id="description"
                  value={currentTutorial.rejestracja}
                  onChange={this.onChangeRejestracja}
                  pattern="[a-z]{2,3}+ [A-Z0-9]{4,6}$"
                />
              </div>
              <div class="imput-group date">
				        <label for="exampleInputEmail1">Data rejestracji</label>
                <input
                  type="text"
                  className="form-control"
                  id="description"
                  value={currentTutorial.data_publikacji}
                />
			        </div>
             
            </form>
            <button
              className="badge badge-danger mr-2"
              onClick={this.deleteTutorial}
            >
              Delete
            </button>

            <button
              type="submit"
              className="badge badge-success"
              onClick={this.updateTutorial}
            >
              Update
            </button>
            <p>{this.state.message}</p>
          </div>
        ) : (
          <div>
            <br />
            <p>Please click on a Tutorial...</p>
          </div>
        )}
      </div>
    );
  }
}