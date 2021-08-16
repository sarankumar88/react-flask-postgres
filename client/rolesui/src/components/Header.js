import PropTypes from 'prop-types';

const Header = ({title}) => {
    return (
        <header className='header'>
            <h1 >{title}</h1>
        </header>
    )
}

Header.defaultProps = {
    'title' : 'Manage Roles'
}

Header.propTypes = {
    title  : PropTypes.string.isRequired
}

// // CSS in JS
// const headingStyle = {
//     'display': 'flex',
//     'justify-content': 'space-between',
//     'align-items': 'center',
//     'margin-bottom': '20px'
//   }
export default Header
