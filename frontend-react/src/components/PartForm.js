import React, {Fragment} from 'react'
import Dropdown from "./Dropdown"


const PartForm = (props) => {
    const {workCenters} = props;

    return (
        <Fragment>
            <div className="fields">
                <div className="twelve wide field">
                    <label>Part Name:</label>
                    <input type="text"/>
                </div>
                <div className="four wide field">
                    <label>Amount:</label>
                    <input type="text"/>
                </div>
            </div>
            <Dropdown
                workCenters={workCenters}
            />
        </Fragment>

    )
};

export default PartForm;
