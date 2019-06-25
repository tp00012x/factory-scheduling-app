import React from 'react'


const Dropdown = (props) => {
    const {workCenters} = props;

    return (
        <div className="field">
            <label>Work Center:</label>
            <select>
                {workCenters.map((workCenter) => {
                    const {pk, name} = workCenter;
                    return <option value={name} key={pk}>{name}</option>
                })}
            </select>
        </div>
    )
};

export default Dropdown;
