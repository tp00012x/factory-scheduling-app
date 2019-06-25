import React, {Component} from 'react'
import Submit from './Submit'
import api from "../api/api";


class SpaceVehicleNameForm extends Component {
    onOrderSubmit = async (e) => {
        e.preventDefault();
        const {setOrderSubmitted, spaceVehicleName} = this.props;

        await api.post('/scheduling/space_vehicle_orders/', {name: spaceVehicleName});

        setOrderSubmitted(true)
    };

    handleOrderChange = (event) => {
        const spaceVehicleName = event.target.value;
        const {setSpaceVehicleName} = this.props;

        setSpaceVehicleName(spaceVehicleName);
    };

    render() {
        const {spaceVehicleName} = this.props;

        return (
            <div className="container d-flex justify-content-center full-height align-items-center">
                <form className="ui form" onSubmit={this.onOrderSubmit}>
                    <h4 className="ui dividing header text-center">Space Vehicle Order</h4>
                    <div className="field">
                        <label>Order Name:</label>
                        <input type="text" onChange={this.handleOrderChange} value={spaceVehicleName}/>
                    </div>
                    <Submit/>
                </form>
            </div>
        )
    }
}

export default SpaceVehicleNameForm;
