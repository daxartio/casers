use pyo3::prelude::*;

/// Convert to camel case.
#[pyfunction]
fn to_camel(s: &str) -> PyResult<String> {
    let mut result = String::with_capacity(s.len());
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

/// Convert to snake case.
#[pyfunction]
fn to_snake(s: &str) -> PyResult<String> {
    let mut result = String::with_capacity(s.len());
    let mut upper_count = 0;
    let mut underscore_count = 0;
    for (i, c) in s.chars().enumerate() {
        if c.is_uppercase() {
            upper_count += 1;
            if i > 0 && upper_count < 2 && underscore_count < 1 {
                result.push('_');
            }
            result.push(c.to_ascii_lowercase());
        } else if c == ' ' || c == '_' || c == '-' {
            if underscore_count < 1 {
                result.push('_');
                underscore_count += 1;
            }
            upper_count = 0;
        } else {
            if upper_count > 1 {
                if let Some(last_c) = result.pop() {
                    if underscore_count < 1 {
                        result.push('_');
                    }
                    result.push(last_c);
                }
            }
            upper_count = 0;
            underscore_count = 0;
            result.push(c);
        }
    }
    Ok(result)
}

/// Casers package.
#[pymodule]
fn _casers(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(to_camel, m)?)?;
    m.add_function(wrap_pyfunction!(to_snake, m)?)?;
    Ok(())
}
