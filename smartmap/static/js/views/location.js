$.shpn.LocationView = Backbone.View.extend({
    template: _.template($('#template-location').html()),
    render: function () {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});
