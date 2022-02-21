import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import * as clanActions from "../../store/clan"

function CreateClan() {
    const dispatch = useDispatch();
    const history = useHistory();
    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [errors, setErrors] = useState([]);
    const [showSucces, setShowSuccess] = useState(false);
    const user = useSelector(state => state.session.user);
    const handleSubmit = (e) => {
        e.preventDefault();
        const payload = {
            user_id: user.id,
            name,
            description
        }
        return dispatch(clanActions.createClan(payload)).then(
            (response) => {
                if (response.errors) {
                    setErrors(response.errors)
                    return
                }
                setShowSuccess(true);
                setTimeout(() => {
                    setShowSuccess(false);
                    history.push(`/clans/${response[clan.id]}`)
                }, 500);
            }
        );
    }

    return (<>
        <div className="header-parent">
            <div className="left-corner"></div>
            <div className="header-child"><h2>Create a Clan</h2></div>
            <div className="right-corner"></div>
        </div>
        <div className="content-container">
            <div className="content">
                {errors.map((error, idx) => (
                    <p key={idx} className="errors">{error}</p>
                ))}
                {showSuccess && (<h2>Success!</h2>)}
                <form onSubmit={(e) => handleSubmit(e)}>
                    <input
                        value={name}
                        type="text"
                        onChange={(e) => setName(e.target.value)}
                        required
                        placeholder="Clan name; Ex: Pepper Ridge Farm"
                    />
                    <textarea
                        value={description}
                        onChange={(e) => setDescription(e.target.value)}
                        placeholder="Clan description (optional)"
                    />
                    <div className="button-div">
                        <button type="submit">SUBMIT</button>
                        <button type="button"
                            onClick={() => {
                                setDescription("");
                                setName("");
                            }}>
                            RESET
                        </button>
                        <button type="button"
                            onClick={() => {
                                setDescription("");
                                setName("");
                            }}
                        >CANCEL</button>
                    </div>
                </form>

            </div>
        </div>
    </>
    )
}

export default CreateClan;