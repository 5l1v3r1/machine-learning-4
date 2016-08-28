/**
 * model_type.jsx: append list of model types.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import checkValidString from './../validator/valid_string.js';

var ModelType = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_model_type: '--Select--'
        };
    },
  // update 'state properties': pass property to parent component
    changeModelType: function(event){
        if (checkValidString(event.target.value)) {
            this.setState({value_model_type: event.target.value});
            this.props.onChange({value_model_type: event.target.value});
        }
        else {
            this.setState({value_model_type: '--Select--'});
        }
    },
  // triggered when 'state properties' change
    render: function(){
      // display result
        return(
            <select
                name='model_type'
                autoComplete='off'
                onChange={this.changeModelType}
                value={this.state.value_model_type}
            >

                <option value='' defaultValue>--Select--</option>
                <option value='svm'>Classification</option>
                <option value='svr'>Regression</option>

            </select>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ModelType
