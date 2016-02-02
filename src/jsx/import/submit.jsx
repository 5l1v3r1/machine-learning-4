/**
 * submit.jsx: append 'submit' button.
 *
 * @Submit, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var Submit = React.createClass({
  // update 'state properties': allow parent component(s) to access properties
     formSubmit: function(event){
        this.props.onChange({created_submit_button: true});
     },
  // triggered when 'state properties' change
    render: function(){
        return(<input type='submit' className='svm-form-submit' onClick={this.formSubmit} />);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default Submit
