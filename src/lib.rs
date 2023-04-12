use pyo3::prelude::*;

/// Convert to camel case.
#[pyfunction]
fn to_camel(s: String) -> PyResult<String> {
    let mut result = String::new();
    let mut capitalize_next = false;
    for c in s.chars() {
        if c == ' ' || c == '_' || c == '-' {
            capitalize_next = true;
        } else {
            if capitalize_next {
                result.push(c.to_ascii_uppercase());
                capitalize_next = false;
            } else {
                result.push(c.to_ascii_lowercase());
            }
        }
    }
    Ok(result)
}

/// Convert from snake to camel case.
#[pyfunction]
fn snake_to_camel(s: &str) -> PyResult<String> {
    let mut result = String::new();
    let mut capitalize_next = false;
    for c in s.chars() {
        if c == '_' {
            capitalize_next = true;
        } else {
            if capitalize_next {
                result.push(c.to_ascii_uppercase());
                capitalize_next = false;
            } else {
                result.push(c);
            }
        }
    }
    Ok(result)
}

/// Casers package.
#[pymodule]
fn _casers(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(to_camel, m)?)?;
    m.add_function(wrap_pyfunction!(snake_to_camel, m)?)?;
    Ok(())
}
