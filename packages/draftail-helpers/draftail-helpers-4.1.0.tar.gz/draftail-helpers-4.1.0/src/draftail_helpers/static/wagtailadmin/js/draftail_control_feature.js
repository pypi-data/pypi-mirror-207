(function(window) {

    const React = window.React;
    const ReactDOM = window.ReactDOM;

    class DraftailControl extends React.Component {

        constructor(props) {
            super(props);

            this.getEditorState = this.getEditorState.bind(this);
            this.updateEditorState = this.updateEditorState.bind(this);

            this.Modifier = window.DraftJS.Modifier;
            this.EditorState = window.DraftJS.EditorState;
            this.SelectionState = window.DraftJS.SelectionState;
        }

        componentDidMount() {
        }

        getEditorState() {
            const { getEditorState } = this.props;
            return getEditorState();
        }

        updateEditorState(newState) {
            const { onChange } = this.props;
            onChange(newState);
        }
    };

    const resolvePath = function (path) {

          var components = path.split(".");

          if( !components ) return null;
          if( components[0] != "window" ) return null;

          components = components.slice(1);

          var result = window;

          for( let index in components ) {

            const component = components[index];
            if( !(component in result)) return null;

            result = result[component];
          }

          return result;
    };

    const resolveControls = function (specifiers) {

        const result = [];

        for( let index in specifiers ) {

            const specifier = specifiers[index];
            var control = specifier["control"];

            if( control == null ) continue;

            control = resolvePath(control);

            if( control == null ) continue;

            control = control(specifier);

            if( control == null ) continue;

            result.push( control );
        }

        return result;
    };

    window.draftailHelpers = window.draftailHelpers || {};
    window.draftailHelpers.DraftailControl = DraftailControl;
    window.draftailHelpers.resolveDraftailControls = resolveControls;

})( typeof window !== "undefined" ? window: this);

