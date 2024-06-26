describe('Attempting to setup prerequisite', () => {
    let uid // user id
    let name // name of the user (firstName + ' ' + lastName)
    let email // email of the user

    before(function () {
        cy.fixture('user.json')
            .then((user) => {
            cy.request({
                method: 'POST',
                url: 'http://localhost:5005/users/create',
                form: true,
                body: user
            }).then((response) => {
                uid = response.body._id.$oid
                name = user.firstName + ' ' + user.lastName
                email = user.email
            })
        })
    });

    beforeEach(function () {
    // enter the main main page and login
        cy.visit('http://localhost:3000')
        cy.contains('div', 'Email Address')
            .find('input[type=text]')
            .type(email)

        cy.get('form')
            .submit()

        cy.get('h1')
            .should('contain.text', 'Your tasks, ' + name)
            cy.get('h1')
            .should('contain.text', 'Your tasks, ' + name);

        cy.get('div')
            .should('have.class', 'container-element')
            .find('form')
            .find('input#title')
            .type('My test item');

        cy.get('div')
            .should('have.class', 'container-element')
            .find('form')
            .find('input#url')
            .type('visa7811n32jkasd8');

        cy.get('div.container-element form').submit();

        cy.get('.container-element').eq(0)
            // Find the <a> element inside the first container-element
            .find('a')
            // Click on the <a> element
            .click();

        cy.get('input[placeholder="Add a new todo item"]')
            .click()
            .type('My new todo item');
        cy.get('form.inline-form input[type="submit"][value="Add"]').click();
        cy.get('ul.todo-list li.todo-item span.editable').contains('My new todo item');
    });

    // test #2.1
    it('Toggle from active to done', () => {
        cy.get('span.checker').should('have.class', 'unchecked').eq(1).as('checkerSpan');
        cy.get('@checkerSpan').click();
        cy.get('@checkerSpan').should('have.class', 'checked');
    });

    // test #2.2
    it('Toggle from done to active', () => {
        cy.get('span.checker').should('have.class', 'checked').eq(1).as('checkerSpan');
        cy.get('@checkerSpan').click();
        cy.get('@checkerSpan').should('have.class', 'unchecked');
    });



    after(function () {
        // clean up by deleting the user from the database
        cy.request({
            method: 'DELETE',
            url: `http://localhost:5005/users/${uid}`
        }).then((response) => {
            cy.log(response.body)
        })
    })
})
