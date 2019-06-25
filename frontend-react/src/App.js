import React, {Component} from 'react';
import api from './api/api'
import SpaceVehicleNameForm from './components/SpaceVehicleNameForm'
import OrderForm from './components/OrderForm'

class App extends Component {
    state = {
        orderSubmitted: false,
        spaceVehicleName: '',
    };

    setOrderSubmitted = (bool) => {
        this.setState({orderSubmitted: bool})
    };

    setSpaceVehicleName = (spaceVehicleName) => {
        this.setState({spaceVehicleName})
    };

    handleSubmit = async (e) => {
        e.preventDefault();
        const {workCenter} = this.state;

        await api.post('/scheduling/work_centers/', {name: workCenter});
    };


    render() {
        const {orderName, orderSubmitted, spaceVehicleName} = this.state;

        return (
            !orderSubmitted ? (
                <SpaceVehicleNameForm
                    orderName={orderName}
                    setOrderSubmitted={this.setOrderSubmitted}
                    setSpaceVehicleName={this.setSpaceVehicleName}
                    spaceVehicleName={spaceVehicleName}
                />
            ) : (
                <OrderForm
                    spaceVehicleName={spaceVehicleName}
                />
            )
        )
    }
}

export default App;
