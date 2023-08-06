(function(window) {

        const StructBlock = window.wagtailStreamField.blocks['StructBlock'];
        const StructBlockDefinition = window.wagtailStreamField.blocks['StructBlockDefinition'];
        const StructBlockValidationError = window.wagtailStreamField.blocks['StructBlockValidationError'];

        class SwitchBlock extends StructBlock {
          constructor(blockDef, placeholder, prefix, initialState, initialError) {
            super(blockDef, placeholder, prefix, initialState, initialError);

            const parentSelector = window.escapeHtml(this.blockDef.meta.classname || '').split(/\s+/).filter(x => !!x).map(x => '.' + x).join("");

            const selectElement = document.querySelectorAll('#' + prefix + '-__type__')[0];
            var options = [];

            const parentElement = selectElement.closest(parentSelector);

            if( parentElement ) {
                options = Array.from(parentElement.children);
                options = options.filter(element => element.dataset.contentpath && element.dataset.contentpath != '__type__');
            }

            const choiceChanged = function (event) {

                const selectedOption = selectElement.options[selectElement.selectedIndex];

                Array.prototype.forEach.call(options, (element, index) => {

                    if( element.dataset.contentpath == selectedOption.value ) {
                        element.style.setProperty("display", "block");
                    } else {
                        element.style.setProperty("display", "none");
                    }
                });
            };

            selectElement.addEventListener("change", choiceChanged, false);
            selectElement.addEventListener("input", choiceChanged, false);
            choiceChanged(null);
          }

          getState() {
            const state = {};
            // eslint-disable-next-line guard-for-in
            for (const name in this.childBlocks) {
              state[name] = this.childBlocks[name].getState();
            }
            return state;
          }

          getValue() {
            const value = {};
            // eslint-disable-next-line guard-for-in
            for (const name in this.childBlocks) {
              value[name] = this.childBlocks[name].getValue();
            }
            return value;
          }
        };

        class SwitchBlockDefinition extends StructBlockDefinition {
          constructor(name, childBlockDefs, meta) {
            super(name, childBlockDefs, meta);
          }

          render(placeholder, prefix, initialState, initialError) {
            return new SwitchBlock(
              this,
              placeholder,
              prefix,
              initialState,
              initialError,
            );
          }
        };

        window.wagtail_switch_block = {};
        window.wagtail_switch_block.SwitchBlock = SwitchBlock;
        window.wagtail_switch_block.SwitchBlockDefinition = SwitchBlockDefinition;
        window.wagtail_switch_block.SwitchBlockValidationError = StructBlockValidationError;

        window.telepath.register(
            'wagtail_switch_block.SwitchBlock',
            SwitchBlockDefinition);

        window.telepath.register(
          'wagtail_switch_block.SwitchBlockValidationError',
          StructBlockValidationError
        );

})( typeof window !== "undefined" ? window: this);

