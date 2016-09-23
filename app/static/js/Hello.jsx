var React = require('react');
var ReactDOM = require('react-dom');


var Hello = React.createClass({
  render: function() {
    return (
      <div className="commentBox">
        Hello, world! I am a CommentBox.
      </div>
    );
  },
});

window.MyApp = {

  init: function (opts) {
    var mountPoint = opts.mount;
    var config = opts.props;
    ReactDOM.render(React.createFactory(Hello)(config), document.getElementById(mountPoint));
  }

};
