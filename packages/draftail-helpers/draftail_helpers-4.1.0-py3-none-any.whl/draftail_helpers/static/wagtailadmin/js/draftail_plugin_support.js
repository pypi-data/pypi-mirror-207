(function(window) {

    const React = window.React;
    const ReactDOM = window.ReactDOM;

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

    const resolvePlugins = function (specifiers) {

        const result = [];

        for( let index in specifiers ) {

            const specifier = specifiers[index];


            var plugin = specifier["plugin"];

            if( plugin == null ) continue;

            plugin = resolvePath(plugin);

            if( plugin == null ) continue;

            plugin = plugin(specifier);

            if( plugin == null ) continue;

            result.push(plugin);
        }

        return result;
    };

    window.draftailHelpers = window.draftailHelpers || {};
    window.draftailHelpers.resolveDraftailPlugins = resolvePlugins;

})( typeof window !== "undefined" ? window: this);

