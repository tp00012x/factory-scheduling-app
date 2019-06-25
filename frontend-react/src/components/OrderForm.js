import React, {Component} from 'react'
import Submit from './Submit'
import api from "../api/api";
import PartForm from "./PartForm"

class OrderForm extends Component {

    state = {
        workCenters: [],
    };


    async componentDidMount() {
        const workCenters = await api.get('/scheduling/work_centers/');

        this.setState({workCenters: workCenters.data});
    }

    render() {
        const {workCenters} = this.state;
        const {spaceVehicleName} = this.props;

        return (
            <div className="container d-flex justify-content-center full-height align-items-center">
                <form className="ui form" onSubmit={this.handleSubmit}>
                    <h4 className="ui dividing header text-center">Space Vehicle Order: {spaceVehicleName}</h4>
                    <PartForm
                        workCenters={workCenters}
                    />
                    <Submit/>
                </form>
            </div>
        )
    }


};

export default OrderForm;
